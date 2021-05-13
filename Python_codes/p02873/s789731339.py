S=input()
num=len(S)
a=[0]*(num+1)
for i in range(num):
  if S[i]=="<":
    a[i+1]=max(a[i+1],a[i]+1)
for i in range(1,num+1):
  if S[-i]==">":
    a[-(i+1)]=max(a[-(i+1)],a[-i]+1)
print(sum(a))
