k,a,b = map(int,input().split())
ans = 0
if a+1 < b:
    k -= a-1
    if k%2 == 1:
        ans = k//2 * b + - (k//2 - 1) * a + 1
    else:
        ans = k//2 * b - (k//2 - 1) * a
else:
    ans = k+1
print(ans)