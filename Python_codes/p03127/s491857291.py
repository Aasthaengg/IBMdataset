import fractions
N = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, N):
    ans = fractions.gcd(ans, a[i])
print(ans)