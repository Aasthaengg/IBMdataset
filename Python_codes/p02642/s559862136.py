N = int(input())
A = list(map(int, input().split()))
Ad = {}
for a in A:
    Ad[a] = Ad.get(a, 0) + 1
A, maxA, ans = sorted(Ad.keys()), max(Ad.keys()), 0

for a in A:
    if Ad[a] == 1:
        ans += 1
    if Ad[a] >= 1:
        if a == 1:
            break
        m = 2
        while a * m <= maxA:
            if a * m in Ad:
                Ad[a * m] = 0
            m += 1

print(ans)
