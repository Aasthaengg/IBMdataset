import fractions
n = int(input())
T = []
ans = 1
for i in range(n):
    t = int(input())
    T.append(t)
    ans = ans * t // fractions.gcd(ans, t)
print(ans)