sl = list(input())
dl = []

n = len(sl)
i = 0
while i < n:

    if i < n-1 and sl[i] == "B" and sl[i+1] == "C":
        dl.append("D")
        i += 2
    else:
        dl.append(sl[i])
        i += 1

ans = 0
c = 0
for d in dl:
    if d == "A":
        c += 1
    elif d == "D":
        ans += c
    else:
        c = 0


print(ans)

