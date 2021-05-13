N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
ans=0
check=10**9
for i in range(N):
  ondo=T-H[i]*0.006
  temp_val=abs(A-ondo)
  if temp_val<check:
    check=temp_val
    ans=i+1
print(ans)
