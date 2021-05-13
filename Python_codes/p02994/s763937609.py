n, l = map(int, input().split())
m = 300
ls = []
for i in range(l, l+n):
    m = i if abs(i) < abs(m) else m
    ls.append(i)
print(sum(ls) - m)