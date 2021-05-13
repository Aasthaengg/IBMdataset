n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
ans = 0

for i in arr:
    x -= i
    if x < 0:
        break
    else:
        ans += 1
if x > 0 and ans > 0:
    ans -= 1

print(ans)