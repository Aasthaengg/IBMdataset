n = int(input())
a = [int(input()) for _ in range(n)]
if a[0] != 0 or any(a[i+1]-a[i]>1 for i in range(n-1)):
    print(-1)
    exit(0)
ans = 0
for i in range(1,n):
    if a[i] == a[i-1] + 1:
        ans += 1
    else:
        ans += a[i]
print(ans)