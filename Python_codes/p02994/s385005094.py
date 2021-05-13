n,l = map(int,input().split())
m = list(range(l,l+n))
if m[-1] < 0:
    m.pop(-1)
    print(sum(m))
elif m[0] > 0:
    m.pop(0)
    print(sum(m))
else:
    print(sum(m))