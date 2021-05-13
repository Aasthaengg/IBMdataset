n=int(input())
#a,b=map(int,input().split())
a=list(map(int,input().split()))
#n=int(input())
#s=input()

sa=sum(a)
ans=10**10+1
x=0
for i in range(0,n-1):
  x+=a[i]
  if abs(2*x-sa)<ans:
    ans=abs(2*x-sa)
print(ans)