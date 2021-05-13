N = int(input())
A = list(map(int, input().split()))
B = [0]*N
for i in range(N):
    B[i] = A[i] - i
B.sort()

res = 0
x = B[N//2]

for i in range(N):
    res += max(x - B[i], -x + B[i])

print(res)