N = int(input())
A = list(map(int, input().split()))

s = sum(A)
res = None
tmp = 10**18

for i in range(N):
    if abs(s - A[i] * N) < tmp:
        tmp = abs(s - A[i] * N)
        res = i

print(res)
