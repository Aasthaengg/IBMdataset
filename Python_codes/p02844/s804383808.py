N = int(input())
S = list(input())

ans = 0

for i in range(1000):
    t = str(i)
    t = t.zfill(3)
    now = t[0]
    count = 0
    for j in S:
        if count == 0 and now == j:
            now = t[1]
            count += 1
            continue
        if count == 1 and now == j:
            now = t[2]
            count += 1
            continue
        if count == 2 and now == j:
            ans += 1
            break

print(ans)