n, k = map(int,input().split())

if k == 0:
    print(n**2)
else:
    ans = 0
    cnt = 1
    for b in range(k+1,n+1):
        ans += cnt*(n//b)
        if (n-b*(n//b))-(k-1) > 0:
            ans += (n-b*(n//b))-(k-1)
        cnt += 1
        #print(ans)
    print(ans)