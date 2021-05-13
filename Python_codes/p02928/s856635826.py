N, K = map(int, input().split())
A = list(map(int, input().split()))
N = int(1e9 + 7)

ans = 0

for i, a in enumerate(A):
    L, R = 0, 0
    for j, b in enumerate(A):
        if b < a:
            if j < i:
                L += 1
            else:
                R += 1
    ans += (L + R) * K * (K - 1) // 2
    ans += R * K

ans = ans % N
print(int(ans))