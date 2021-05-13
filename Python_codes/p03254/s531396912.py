import sys
N, x = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) == x:
    print(N)
    sys.exit()
else:
    a.sort()
    ans = 0
    for i in range(N-1):
        if a[i] <= x:
            ans += 1
            x -= a[i]
        else:
            print(ans)
            break
    else:
        print(ans)