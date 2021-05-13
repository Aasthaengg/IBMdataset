import sys
input = sys.stdin.readline

L = str(int(input()))
N = len(L)
MOD = 10**9 + 7

smaller = [0] * N
not_smaller = [0] * N

smaller[0] = 1
not_smaller[0] = 2

for i in range(1, N):
    if L[i] == "1":
        smaller[i] = 3 * smaller[i - 1] + not_smaller[i - 1]
        not_smaller[i] = 2 * not_smaller[i - 1]
    elif L[i] == "0":
        smaller[i] = 3 * smaller[i - 1]
        not_smaller[i] = not_smaller[i - 1]

    smaller[i] %= MOD
    not_smaller[i] %= MOD

ans = (smaller[-1] + not_smaller[-1]) % MOD
print(ans)
