N = int(input())
S = input()

ans = 0
for d1 in "0123456789":
    p1 = S.find(d1)
    if p1 == -1: continue

    for d2 in "0123456789":
        p2 = S[p1+1:].find(d2)
        if p2 == -1: continue

        for d3 in "0123456789":
            if d3 in S[p1+p2+2:]:
                ans += 1

print(ans)

