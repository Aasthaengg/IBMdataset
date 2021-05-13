S = input()
s = S.replace("BC", "X")
ans = 0
a = 0
for c in s:
    if c == "A":
        a += 1
    elif c == "X":
        ans += a
    else:
        a = 0

print(ans)