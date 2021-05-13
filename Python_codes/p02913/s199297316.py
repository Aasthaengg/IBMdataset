n=int(input())
ss=input()

# Z-algorithm
# 文字列が与えられた時、各 i について「S と S[i:|S|-1] の最長共通接頭辞の長さ」を記録した配列 A を O(|S|) で構築するアルゴリズムです。
#s='aaabaaaab'
def func(s):
  a=[0]*len(s)
  a[0]=len(s)
  i,j=1,0
  while i<len(s):
    while i+j<len(s) and s[j]==s[i+j]:
      j+=1
    a[i]=j
    if j==0:
      i+=1
      continue
    k=1
    while i+k<len(s) and k+a[k]<j:
      a[i+k]=a[k]
      k+=1
    i+=k
    j-=k
  return a
ans=0
for i in range(n):
  a=func(ss[i:])
  for j in range(len(a)):
    ans=max(ans,min(a[j],j))
print(ans)
