n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(n,3*n,2):
    ans += a[i]
print(ans)