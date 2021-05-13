N = int(input())
A = [0,0] + list(map(int, input().split()))

lis = [0]*(N+1)
for i in range(2,N+1):
    lis[A[i]] += 1

for i in range(1,N+1):
    print(lis[i])