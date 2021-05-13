n,t=map(int,input().split())
A=list(map(int,input().split()))

b=A[0]
B=[b]*(n-1)
for i in range(1,n):
  b=min(b,A[i])
  B[i-1]=A[i]-b
print(B.count(max(B)))