S = input()
cnt = 0
ans = 0
S = S.replace("BC","X")
S += "."
for s in S:
    if s == "X":
        ans += cnt
    elif s == "A":
        cnt += 1
    else:
        cnt = 0
print(ans)