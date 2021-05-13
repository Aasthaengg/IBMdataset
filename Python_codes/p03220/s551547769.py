n=int(input())
t,a=map(int, input().split())
h=list(map(int, input().split()))
ans=0
cnt=100000000
for i in range(n):
  if abs(a-t+(h[i]*0.006))<cnt:
    cnt=abs(a-t+(h[i]*0.006))
    ans=i
print(ans+1)