S = input()
S = S.replace("BC", "D")
segs = []
prev = "a"
for c in S:
    if c in "AD":
        if prev not in "AD":
            segs.append([c])
        else:
            segs[-1].append(c)
    prev = c

ans = 0
for seg in segs:
    pos = []
    for i in range(len(seg)):
        if seg[i] == "D":
            pos.append(i)
    for i, p in enumerate(pos):
        ans += p - i

print(ans)
