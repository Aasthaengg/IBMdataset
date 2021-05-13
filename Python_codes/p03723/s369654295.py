def ave(b,c):
    return b//2 + c//2
def rest(a,b,c):
    return ave(b,c), ave(a,c), ave(b,a)
a, b, c = map(int, input().split())
ans = 0
while 1:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1 :
        print(ans)
        break
    d, e, f = rest(a,b,c)
    if (a, b, c) == (d, e, f):
        print(-1)
        break
    ans += 1
    a, b, c = d, e, f