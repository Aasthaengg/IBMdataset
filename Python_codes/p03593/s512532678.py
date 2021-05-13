t="abcdefghijklmnopqrstuvwxyz"
h,w=map(int,input().split())
a=[list(input())for _ in range(h)]
b=[0]*26
for i in a:
  for j in i:b[t.index(j)]+=1
x,y,z=(h//2)*(w//2),(h%2)*(w//2)+(h//2)*(w%2),(h%2)*(w%2)
for i in b:
  j=i
  while x and j>3:
    x-=1
    j-=4
  while y and j>1:
    y-=1
    j-=2
  z-=j
if not(x==y==z==0):print("No")
else:print("Yes")
"""#一例出力、問題誤読して実装した
c=[w*[0]for _ in range(h)]
fi=ti=0
for i in range(27):
  while b[i]:
    if b[i]>=4:
      j,k=fi//(w//2),fi%(w//2)
      c[j][k]=c[j][w-k-1]=c[h-j-1][k]=c[h-j-1][w-k-1]=t[i]
      fi+=1
      b[i]-=4
    if b[i]==2:
      if ti<h//2 and w%2:c[ti][w//2]=c[h-ti-1][w//2]=t[i]
      else:c[h//2][ti]=c[h//2][w-1-ti]=t[i]
      ti+=1
      b[i]-=2
    if b[i]==1:
      c[h//2][w//2]=t[i]
      b[i]-=1
for i in c:print("".join(i))
"""