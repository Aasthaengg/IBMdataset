a, b, k = list(map(int, input().split()))

if (b - a) <= k:
    for i in range(a, b + 1):
        print(i)
    exit()

ans = set()
for i in range(k):
    ans.add(a + i)
for i in range(k):
    ans.add(b - i)

ans = sorted(ans)

for a in ans:
    print(a)
