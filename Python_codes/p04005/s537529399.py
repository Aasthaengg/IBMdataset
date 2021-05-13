A = sorted(list(map(int, input().split())))
print(0 if any([a % 2 == 0 for a in A]) else A[0] * A[1])
