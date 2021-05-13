S = input()

b_cumsum = [0] * len(S)
now = 0
for i in range(len(S)):
    if S[i] == "B":
        b_cumsum[i] = now + 1
        now += 1
    else:
        b_cumsum[i] = now

S = S[::-1]
b_cumsum = b_cumsum[::-1]
ans = 0
for i, s in enumerate(S):
    if s == "W":
        ans += b_cumsum[i]

print(ans)
