n, x = map(int, input().split())
l = list(map(int, input().split()))
di = 0
ans = 1
for i in range(n):
    di = di + l[i]
    if di > x:
        break
    ans += 1
print(ans)
