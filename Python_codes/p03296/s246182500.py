N = int(input())
a = list(map(int,input().split()))
f = 0
ans = 0
for k in range(1,N):
    if a[k] == a[k-1] and f == 0:
        ans += 1
        f = 1
    else:
        f = 0
print(ans)
