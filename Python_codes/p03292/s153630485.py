from itertools import permutations
A = list(map(int, input().split()))
res = 10 ** 4
for perm in permutations(list(range(3))):
    tmp = 0
    for i in range(1, 3):
        tmp += abs(A[perm[i]] - A[perm[i-1]])
    res = min(res, tmp)
print(res)