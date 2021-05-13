N=int(input())
A=input()
B=input()
k=0
for i in range(N):
   if A[N-i-1:N+1]==B[0:i+1]:
      k=i+1
print(N*2-k)
