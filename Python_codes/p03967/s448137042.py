S = input()

cur = "g"
acd = 0
tcd = 0
for c in S:
    if cur != c:
        if cur == "p":
            acd += 1
        else:
            tcd += 1
    cur = "p" if cur == "g" else "g"
print(acd - tcd)
