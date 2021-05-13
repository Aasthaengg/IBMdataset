import fractions

N = int(input())
ans = 1
for _ in range(N):
    T = int(input())
    ans = (ans * T) // fractions.gcd(ans, T)
print(ans)
