S = input()
S = S.replace("BC", "X")
n = len(S)
ans = 0
cnt_a = 0

for s in S:
    if s == "X":
        ans += cnt_a
    elif s == "A":
        cnt_a += 1
    else:
        cnt_a = 0

print(ans)
