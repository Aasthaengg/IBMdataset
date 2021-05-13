n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7
ans = 0
two = 1
for i in range(61):
    one = 0
    for j in range(n):
        if (a[j] >> i) & 1:
            one += 1
    ans = (ans + (one*(n-one))*two) % mod
    two = (two * 2) % mod
print(ans)