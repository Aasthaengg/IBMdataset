x, k ,d = map(int, input().split())
x=abs(x)
if k*d <= x:
    print(x-k*d)
else:
    xx = x
    x -= min(k, x//d)*d
    k -= min(k, xx//d)
    if k % 2 != 0:
        ans = min(abs(x-d),abs(x+d))
    else:
        ans = min(abs(x), abs(x-2*d))
    print(ans)