
N = int(input())
X = list(map(int, input().split()))

total = 0
for a in X:
    total ^= a

ans = []
for a in X:
    ans.append(a ^ total)

print(*ans)

