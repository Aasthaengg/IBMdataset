n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
comp=t-a
ans=0
for i in range(1,n):
  if abs(h[ans]*0.006-comp) > abs(h[i]*0.006-comp):
    ans = i
print(ans+1)