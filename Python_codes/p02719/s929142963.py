n, k = map(int,input().split())
if n % k == 0:
    ans = 0
else:
    ans = min(n % k , k - n % k)
print(ans)