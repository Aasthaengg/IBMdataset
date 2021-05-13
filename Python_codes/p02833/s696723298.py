N = int(input())
if N%2==1:
    print(0)
else:
    ans = 0
    l = []
    N//=2
    n = len(str(N))
    while True:
        a = N//5
        ans += a
        N = a
        if a==0:
            break
    print(ans)