N, M, X = map(int, input().split())
A = list(map(int, input().split()))
left, right = 0, 0
for i in range(X-1, -1, -1):
    if i in A:
        left += 1
for i in range(X+1, N+1):
    if i in A:
        right += 1
print(min(left, right))
