n = int(input())
As = list(map(int, input().split()))
    
def f(m):
    debug = m
    for a in As:
        i = m // a
        m = i * a
    return m

# 二部探索?
l = 1
r = 10**20
while r-l > 1:
    m = (r+l)//2
    if f(m) <= 1: l = m
    else: r = m
ans1 = r
l = 1
r = 10**20
while r-l > 1:
    m = (r+l)//2
    if f(m) <= 2: l= m
    else: r = m
ans2 = l

if ans1 > ans2:
    print(-1)
else:
    print(ans1,ans2)