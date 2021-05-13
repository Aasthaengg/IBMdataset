n = int(input())
s = input()

while len(s) >= 1 and s[0] == ".":
    s = s[1:]

while len(s) >= 1 and s[-1] == "#":
    s = s[:-1]

d = []
cur = "#"
strk = 1

bl = 0
wr = 0

if len(s) > 1:
    for i in range(1, len(s)):
        if s[i] == cur:
            strk += 1
        else:
            d.append((cur, strk))
            if cur == ".":
                wr += strk

            cur = s[i]
            strk = 1

    d.append((cur, strk))
    if cur == ".":
        wr += strk

ans = wr
for i in range(len(d)):
    if d[i][0] == "#":
        bl += d[i][1]
    else:
        wr -= d[i][1]

    ans = min(ans, bl + wr)

print(ans)