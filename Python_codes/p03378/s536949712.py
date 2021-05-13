N, M, X = map(int, input().split())
A = list(map(int, input().split()))


left = 0
right = 0

for a in A:
    if a > X:
        right += 1
    else:
        left += 1
print(min(left, right))
