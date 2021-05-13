while True:
    n = int(input())
    if n==0:break
    s = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += (s[i]-sum(s)/n)**2
    ans = (ans/n)**0.5
    print(ans)
