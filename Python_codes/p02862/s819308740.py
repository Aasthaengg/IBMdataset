x,y = map(int,input().split())
def comb(n,m,p=10**9+7):
    if n < m : return 0
    if n < 0 or m < 0:return 0
    m = min(m, n-m)
    top = bot = 1
    for i in range(m):
        top = top*(n-i) % p
        bot = bot*(i+1) % p
    bot = pow(bot, p-2, p)
    return top*bot % p
if 1/2 <= y/x <= 2 and (x+y)/3 % 1 == 0:
    yy = int((x+y)/3)
    u = int(y - yy)
    r = int(yy - u)
    print(comb(yy,r)%(10**9+7))
else:
    print(0)