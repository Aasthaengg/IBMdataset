n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
if a[0]>0:
    print(-1)
    exit(0)
ans = 0
for i in range(n-1):
    if a[i]+1<a[i+1]:
        print(-1)
        exit(0)
    if a[i]>=a[i+1]:
        ans += a[i]
ans += a[-1]
print(ans)