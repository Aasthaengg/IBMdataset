S = input()
rev_S = S.replace("x", "")

if rev_S != rev_S[::-1]:
    print(-1)
    exit()

res = 0

N = len(S)
l, r = 0, N - 1
while l < r:
    if S[l] == S[r]:
        l, r = l + 1, r - 1
    elif S[l] == "x":
        l += 1
        res += 1
    elif S[r] == "x":
        r -= 1
        res += 1

print(res)
