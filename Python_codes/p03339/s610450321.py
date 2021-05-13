N = int(input())
S =input()
wn = [0] * (N + 1)
en = [0] * (N + 1)
for i in range(1, N + 1):
    if S[i - 1] == 'W':
        wn[i] = wn[i - 1] + 1
        en[i] = en[i - 1]
    else:
        wn[i] = wn[i - 1]
        en[i] = en[i - 1] + 1
ans = [wn[i] + en[N] - en[i + 1] for i in range(N)]
print(min(ans))
