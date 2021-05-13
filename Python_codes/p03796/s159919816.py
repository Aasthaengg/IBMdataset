import sys

N = int(sys.stdin.readline())
ans = 1
MOD = 10 ** 9 + 7
for i in range(1, N + 1):
    ans = ans * i % MOD
print(ans)