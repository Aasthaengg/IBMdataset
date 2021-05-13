n,m = map(int,input().split())
l = [0] * m
r = [0] * m
l_max = 1
r_min = n
for i in range(m):
    l[i], r[i] = map(int,input().split())
    l_max = max(l[i],l_max)
    r_min = min(r[i], r_min)
if r_min >= l_max:
    print(r_min - l_max + 1)
else:
    print(0)