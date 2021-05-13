n=int(input())
t,a=map(int,input().split())
H=list(map(int,input().split()))

m=float('inf')
for i in range(n):
  if abs(a-t+0.006*H[i])<m:
    m=abs(a-t+0.006*H[i])
    ans=i
print(ans+1)