N, M, X = map(int, input().split())
A = list(map(int, input().split()))
i = 0
j = 0
for a in A:
    if a < X:
        i += 1
    elif a > X:
        j += 1
print(min(i, j))
