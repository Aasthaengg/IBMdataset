N=int(input())
A=list(map(int,input().split()))

for i in range(1,N+1):
  A[i-1]-=i
A.sort()
#print(A,(N-N%2)//2)
m=A[(N-N%2)//2]
#print(m)

A=list(map(lambda x: abs(x-m),A))
print(sum(A))