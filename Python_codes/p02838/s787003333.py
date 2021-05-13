N = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7

b = [0] * 65

for i in range(N):
    bb = format(A[i], "060b")
    for j in range(60):
        if bb[j] == "1":
            b[j] += 1

ans = 0

for j in range(60):
    ans = (ans + b[j] * (N - b[j]) * pow(2, 59 - j, mod)) % mod

print(ans)