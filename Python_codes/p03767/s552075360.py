N = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0

for i in range(-2, -2 * N - 1, -2):
    ans += a[i]
    # print(a[i])

print(ans)
