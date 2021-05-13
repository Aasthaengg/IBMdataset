k = int(input())
a = list(map(int, input().split()))

mx = 3
mn = 2
for i in range(k)[::-1]:
    mn = (mn + a[i] - 1) // a[i] * a[i]
    # print(mx + a[i] - 1)
    mx = (mx + a[i] - 1) // a[i] * a[i]
    # mx = min(2 * a[i] - 1, 2 * mx - 1)
    # print(mn, mx)
mx -= 1
# print()

ans = (mn,mx)
for i in range(k):
    mx = (mx // a[i]) * a[i]
    mn = (mn // a[i]) * a[i]
# print(mn, mx)

if mn == 2 and mx == 2:
    print(*ans)
else:
    print(-1)
