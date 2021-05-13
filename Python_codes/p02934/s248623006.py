N = int(input())
A = [int(N) for N in input().split()]
temp = 0

for i in range(0,N):
  temp=temp+(1/A[i])
print(1/temp)