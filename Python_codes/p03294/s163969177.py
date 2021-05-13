N = int(input())
arr = list(map(int, input().split()))
ans = 0
m = 1
for num in arr:
    m *= num

for num in arr:
    ans += (m - 1) % num

print(ans)
