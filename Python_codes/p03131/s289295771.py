#みんなのプロコン2019-C
k,a,b = map(int,input().split())

if b - a <= 2:
    print(k+1)
else:
    r = k - (a-1)
    ans = max(0,a + r//2*(b-a)+r%2)
    print(ans)