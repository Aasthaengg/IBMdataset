N = int(input())
A = list(map(int,input().split()))

mul = 1
for i in A:
    mul *= i 

m = 0
for i in range(N):
    m += mul // A[i]

print(mul / m)
