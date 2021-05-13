S = input()
n = len(S)
n = n - 2 if n % 2 == 0 else n - 1
ans = -1
for i in range(n - 1, -1, -2):
    T = S[: i + 1]
    l = (i + 1) // 2
    if T[: l] == T[l:]:
        ans = i + 1
        break
print(ans)