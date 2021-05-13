N = int(input())
lr = []
for _ in range(N):
    lr.append(tuple(map(int, input().split())))

ans = 0
for el in lr:
    l, r = el
    ans += r - l + 1
print(ans)