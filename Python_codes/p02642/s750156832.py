N = int(input())
A = list(map(int, input().split()))

maxA = max(A)
memo = [0] * (maxA + 1)

seen = set()
for a in A:
    for mul_a in range(a, maxA+1, a):
        if a not in seen and mul_a == a: 
            continue
        memo[mul_a] += 1
    seen.add(a)

ans = 0
seen = set()
for a in A:
    if memo[a] == 0 and a not in seen:
        seen.add(a)
        ans += 1

print(ans)
