n, m = map(int, input().split())
n_l = []
ans = [0, 0, 0]

for _ in range(n):
    l = list(map(int, input().split()))
    n_l.append(l)
for x in range(m):
    p = int(input())
    for o in range(n):
        n_l[o][x] *= p
for i in n_l:
    print(sum(i))
