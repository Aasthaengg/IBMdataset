import sys

n = int(input())
a = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    if i == 0:
        if a[i] != 0:
            ans = -1
            break
    elif a[i] > i:
        ans = -1
        break

    else:
        if a[i] == a[i-1] + 1:
            continue
        else:
            if a[i] >= a[i-1] + 2:
                ans = -1
                break
            ans += a[i-1]

if ans == -1:
    print(-1)
    sys.exit()

ans += a[n-1]

print(ans)
