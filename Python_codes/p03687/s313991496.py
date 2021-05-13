S = input()

tmp = 0
length = 0
ans = 100
for s in S:
    for t in S:
        if t != s:
            tmp += 1
        else:
            length = max(tmp, length)
            tmp = 0
    else:
        length = max(tmp, length)
        tmp = 0
    ans = min(ans, length)
    length = 0

print(ans)