N = int(input())
n = 1e5
for i in range(1, N):
    A = i
    B = N - A
    s = 0
    while A > 0:
        s += A % 10
        A = int(A / 10)
    while B > 0:
        s += B % 10
        B = int(B / 10)
    n = min(n, s)
print(n)