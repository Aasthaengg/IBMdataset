N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N)]
ab.sort(key=lambda x: sum(x), reverse=True)
ans = 0
for i, x in enumerate(ab):
    ans += -x[1] if i % 2 else x[0]
print(ans)
