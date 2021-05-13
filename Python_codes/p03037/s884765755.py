n, m = map(int, input().split())
inf = 0
sup = 100001
for i in range(m) :
    l, r = map(int, input().split())
    inf = max(inf, l)
    sup = min(sup, r)
if sup >= inf :
    print(sup-inf+1)
else :
    print("0")
