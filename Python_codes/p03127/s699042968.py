import fractions

N = int(input())
A = list(input().split())
monster = list(sorted([int(A[i]) for i in range(N)]))
ans = float('inf')
MIN = monster[0]

for i in range(N):
    tmp = monster[i]
    ans = min(ans, int(fractions.gcd(tmp, MIN)))

print(ans)