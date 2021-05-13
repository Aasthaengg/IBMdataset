n,m = map(int,input().split())
lst_l = []
lst_r = []
for _ in range(m):
    l,r = map(int,input().split())
    lst_l.append(l)
    lst_r.append(r)

max_l = max(lst_l)
min_r = min(lst_r)

count = 0
for i in range(n):
    if max_l <= i+1 <= min_r:
        count += 1

print(count)