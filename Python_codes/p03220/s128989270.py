n=int(input())
t,a=map(int,input().split())
x=list(map(int,input().split()))
ans=0
cnt=10**3
for i in range(len(x)):
  s=t-x[i]*0.006
  if abs(s-a)<cnt:
    cnt=abs(s-a)
    ans=i+1
print(ans)
