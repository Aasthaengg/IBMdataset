N, P = map(int, input().split())
S = input()
ans = 0
if P == 2:
    for i, d in enumerate(S):
        if d in "02468":
            ans += i + 1
elif P == 5:
    for i, d in enumerate(S):
        if d in "05":
            ans += i + 1
else:
    x = 1
    curr = 0
    mods = [0] * P
    mods[0] = 1
    for d in reversed(S):
        curr = (curr + x * int(d)) % P
        ans += mods[curr % P]
        mods[curr % P] += 1
        x = x * 10 % P
print(ans)
