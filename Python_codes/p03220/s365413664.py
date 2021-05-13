N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
ans=10**9
T=T*1000
A=A*1000
j=0
for i in range(N):
  if abs(A-(T-6*H[i]))<=ans:
    ans=abs(A-T+6*H[i])
    j=i
print(j+1)