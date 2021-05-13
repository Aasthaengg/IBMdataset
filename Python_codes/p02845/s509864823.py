MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))

colors = [0]*3
ans = 1
for i in range(n):
    c = colors.count(A[i])
    ans = ans*c % MOD
    if c == 0:
        break
    colors[colors.index(A[i])] += 1

print(ans % MOD)