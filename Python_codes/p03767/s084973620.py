N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
a_m = a[1::2]
ans = 0
for i in range(N):
    ans += a_m[i]
print(ans)