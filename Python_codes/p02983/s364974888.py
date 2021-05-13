l, r = map(int, input().split())

if l//2019 != r//2019:
    print(0)
else:
    ans = float('inf')
    for i in range(l,r):
        for j in range(l+1,r+1):
            ans = min(i*j%2019,ans)
    print(ans)