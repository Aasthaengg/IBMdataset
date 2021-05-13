N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
ans=0;m=100000000
A=A*1000;T=T*1000
for i in range(N):
    if abs(A-(T-(H[i]*6))) < m:m=abs(A-(T-(H[i]*6)));ans=i+1
print(ans)