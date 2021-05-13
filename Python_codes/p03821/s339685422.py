N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.reverse()
B.reverse()

res = 0
for i in range(N):
    res += (B[i] - (A[i]+res)%B[i]) % B[i]

print(res)