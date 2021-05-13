n=int(input())
tc = 0
hc = 0
for _ in range(0,n):
    t,h = input().split()
    if t > h: tc = tc + 3
    if t < h: hc = hc + 3
    if t == h: 
        tc = tc + 1
        hc = hc + 1
print('{0} {1}'.format(tc, hc))