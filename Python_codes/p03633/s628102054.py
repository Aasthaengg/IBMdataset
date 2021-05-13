import fractions
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

ans = lst[0]
for i in range(1, N):
    ans = ans * lst[i] // fractions.gcd(ans, lst[i])
print(ans)