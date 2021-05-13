n = int(input())
l, r = zip(*[map(int, input().split()) for _ in range(n)])
ans = 0
for i in range(n):
    ans += r[i] - l[i] + 1
print(ans)
