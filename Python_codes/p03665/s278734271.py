import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,p = map(int,input().split())
s = list(map(int,input().split()))
x,y,ans = 0,0,0
for i in s:
    if i%2 == 0:
        x += 1
    else:
        y += 1

if p == 1:
    k = 0
    for i in range(1,y+1,2):
        k += comb(y,i)
    g = 0
    for i in range(x+1):
        g += comb(x,i)
    print(k*g)
else:
    g = 0
    for i in range(x+1):
        g += comb(x,i)
    k = 0
    for i in range(0,y+1,2):
        k += comb(y,i)
    print(k*g)