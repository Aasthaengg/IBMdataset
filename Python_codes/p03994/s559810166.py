S = list(input())
k = int(input())

alp = "abcdefghijklmnopqrstuvwxyza"
to_a = {alp[i]: 26 - i for i in range(1, len(alp))}

for i, s in enumerate(S):
    if to_a[s] > k:
        continue
    else:
        S[i] = "a"
        k -= to_a[s]
    if k == 0:
        break

k %= 26
i = alp.index(S[-1]) + k
S[-1] = alp[i]

ans = "".join(S)
print(ans)
