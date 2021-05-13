N = int(input())
a = [int(input()) for i in range(N)]
if a[0] > 0:
    print(-1)
    exit()

ans = 0
for i in range(1, N):
    if a[i - 1] + 1 < a[i]:
        print(-1)
        exit()
    elif a[i - 1] + 1 == a[i]:
        ans += 1
    else:
        ans += a[i]

print(ans)