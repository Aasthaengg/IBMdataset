n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (10**5+1)
for v in a:
    cnt[v] += 1

res = 0
even = 0
for c in cnt:
    if c > 0:
        if c % 2 == 0:
            even += 1
        res += 1

if even % 2 == 0:
    print(res)
else:
    print(res - 1)