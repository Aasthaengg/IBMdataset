N = int(input())
a = list(map(int, input().split()))
ans = 0
for n in range(1, N):
    if a[n-1] == a[n]:
        ans += 1
        a[n] = "n"
print(ans)