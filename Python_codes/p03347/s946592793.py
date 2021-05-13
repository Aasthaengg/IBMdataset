n = int(input())
a = [int(input()) for _ in range(n)] + [0]
if a[0] > 0:
    print(-1)
else:
    ans = 0
    for i in range(n):
        if a[i] < a[i + 1] - 1:
            print(-1)
            break
        elif a[i] >= a[i + 1]:
            ans += a[i]
    else:
        print(ans)
