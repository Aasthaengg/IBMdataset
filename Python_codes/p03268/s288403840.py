n, k = map(int, input().split())
if k%2 == 1:
    ans = (n//k)**3
    print(ans)
else:
    c = 0
    for i in range(1, n+1):
        if i%k == k//2:
            c += 1
    ans = c**3
    ans += (n//k)**3
    print(ans)
