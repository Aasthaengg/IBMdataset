inp = list(input())

del inp[-1]

ans = 0
S = ""

for s in inp:
    S += s
    N = len(S)
    if N % 2 == 1:
        continue
    if S[:N // 2] == S[N // 2:]:
        ans = max(ans, N)

print(ans)
