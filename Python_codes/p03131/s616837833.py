k,a,b = map(int,input().split())
if b - a <= 1 or a >= k:
    print(k+1)
else:
    k -= a - 1
    ans = a
    ans += (b - a)*(k//2)
    if k % 2 != 0:
        ans += 1
    print(ans)