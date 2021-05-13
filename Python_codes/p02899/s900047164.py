
N = int(input())
X = list(map(int, input().split()))

ans = []
for i, _ in sorted(enumerate(X), key=lambda x: x[1]):
    ans.append(i + 1)

print(*ans)
