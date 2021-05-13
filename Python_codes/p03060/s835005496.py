n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

d = [v[i] - c[i] for i in range(n)]
res = 0
for i in range(n):
    if d[i] > 0:
        res += d[i]

print(res)