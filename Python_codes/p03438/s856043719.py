(n,),aa,bb = [list(map(int, s.split())) for s in open(0)]

up = down = 0

for i in range(n):
    a = aa[i]
    b = bb[i]
    if a > b:
        down += a-b
    if b > a:
        d,m = divmod(b-a,2)
        up += d+m
        down += m

diff = sum(bb) - sum(aa)

if up <= diff and down <= diff:
    print('Yes')
else:
    print('No')