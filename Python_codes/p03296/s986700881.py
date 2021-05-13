n = int(input())
a = list(map(int, input().split()))
ans = 0
if a[0] == a[1]:
    ans = 1
    a[1] = -1000
for i in range(n-1):
    if a[i] == a[i+1]:
        ans += 1
        a[i+1] = -i
print(ans)