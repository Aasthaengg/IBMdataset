n = int(input())
a = sorted(map(int, input().split()))
ans = 0
l = 0
r = 3*n-1
while l < r:
    ans += a[r-1]
    l += 1
    r -= 2
    # print(l, r)

print(ans)