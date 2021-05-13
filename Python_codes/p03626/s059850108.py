N = int(input())
S = [input() for _ in range(2)]

ans = 0
mod = 10 ** 9 + 7
prev = False
cur = False
for i in range(N):
    if cur:
        cur = False
        continue

    if S[0][i] == S[1][i]:
        if i == 0:
            ans = 3
        elif not prev:
            ans = ans * 2 % mod
        cur = False
        prev = False
    else:
        if i == 0:
            ans = 6
        elif prev:
            ans = ans * 3 % mod
        else:
            ans = ans * 2 % mod
        cur = True
        prev = True

print(ans)
