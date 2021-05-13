n = int(input())
t = list(map(int, input().split()))
m = int(input())

sum_t = sum(t)

res = []
for _ in range(m):
    p, x = map(int, input().split())
    res.append(sum_t + (x - t[p-1]))

for v in res:
    print(v)