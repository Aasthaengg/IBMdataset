n = int(input())
P = list(map(int, input().split()))

minimum = 2e6
ans = 0

for p in P:
    if p <= minimum:
        minimum = p
        ans += 1

print(ans)
