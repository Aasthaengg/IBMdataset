N=int(input())
ans=''
a=-2
r=abs(N%a)
q=(N-r)//a
while q!=0:
  ans=str(r)+ans
  N=q
  r=abs(N%a)
  q=(N-r)//a
ans=str(r)+ans
print(ans)