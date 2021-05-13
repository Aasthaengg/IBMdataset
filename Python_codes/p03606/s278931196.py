n = int(input())
lr = []
for _ in range(n):
    a = [int(x) for x in input().split()]
    lr.append(a)

ans = 0

for x in lr:
    ans += x[1] - x[0] + 1
print(ans)