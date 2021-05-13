k,a,b = map(int,input().split())
ans = 1
cnt = 0
m = 0

if a-1 >= k:
    print(k+1)
else:
    cnt += a-1
    ans += a-1
    if a+2 < b:
        m = k - cnt
        cnt += (m // 2) * 2
        ans += (b-a) * (m // 2)

        if cnt != k:
            ans += 1
        print(ans)
    else:
        print(k+1)
