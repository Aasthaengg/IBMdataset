N, M = map(int, input().split())

l_max = 1
r_min = N
for _ in range(M):
    l, r = map(int, input().split())
    l_max = max(l_max, l)
    r_min = min(r_min, r)

if r_min < l_max:
    print(0)
else:
    print(r_min-l_max+1)