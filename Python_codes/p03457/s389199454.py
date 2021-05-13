N=int(input())
flag='Yes'
p,q,r=0,0,0
for _ in range(N):
  t,x,y=map(int,input().split())
  a=abs(x-p)+abs(y-q)
  e=t-r
  if a<=e:
    if (e-a)%2!=0:
      flag='No'
      break
  else:
    flag='No'
    break
  p,q,r=x,y,t
print(flag)