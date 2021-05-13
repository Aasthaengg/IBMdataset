n=int(input())
s=input()

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2

ans=''
for i in s:
  inx=abc.index(i)
  inx+=n
  ans+=abc[inx]

print(ans)