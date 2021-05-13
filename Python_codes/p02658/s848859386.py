n = int(input())
a = list(map(int,input().split()))

judge = True
ans = 0

if 0 not in a:
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            judge = False
            break
        
if judge:
    print(ans)
else:
    print(-1)