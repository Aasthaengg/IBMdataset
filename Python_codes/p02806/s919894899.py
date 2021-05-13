n=int(input())
s=['']*n
a=[0]*n
for i in range(n):
  s[i],v=input().split()
  a[i]=int(v)
x=input()
flg=False
ans=0
for i in range(n):
  if flg:
    ans+=a[i]
  if s[i]==x:
    flg=True
print(ans)
