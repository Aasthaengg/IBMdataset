n, p = map(int, input().split())
a = list(map(int, input().split()))

def comb(n, r):
    ans = 1
    if n < 2*r:
        r = n - r
    for i in range(r):
        ans *= (n - i)
        ans //= (i + 1)
    return ans

ev, od = 0, 0
for i in a:
    if i%2 == 0:
        ev += 1
    else:
        od += 1
ans = 0
if p == 0:
    for i in range(0, od+1, 2):
        for j in range(ev+1):
            ans += comb(od, i)*comb(ev, j)
else:
    for i in range(1, od+1, 2):
        for j in range(ev+1):
            ans += comb(od, i)*comb(ev, j) 
print(ans)