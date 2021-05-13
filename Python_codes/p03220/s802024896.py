N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
c=100000
ans=0
for i in range(N):
  if c>abs(T-H[i]*0.006-A):
    c=abs(T-H[i]*0.006-A)
    ans=i+1
print(ans)