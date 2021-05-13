import fractions

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

ans = a[0]
for i in range(1, n):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print(ans)