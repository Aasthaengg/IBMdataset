S = input()
S = S.replace("BC", "D")
cur = 0
ans = 0
for c in S:
    if c == "A":
        cur += 1
    elif c == "D":
        ans += cur
    else:
        cur = 0
print(ans)
