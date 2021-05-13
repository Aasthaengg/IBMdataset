n=int(input())
b,u=map(int,input().split())
x,c,v=1,1,1
for i in range(n-1):
  a,t=map(int,input().split())
  c=b if b%a==0 else (b//a+1)*a
  v=u if u%t==0 else (u//t+1)*t
  x=max(c//a,v//t)
  b=a*x
  u=t*x
print(b+u)