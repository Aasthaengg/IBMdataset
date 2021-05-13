from itertools import permutations
A = list(map(int, input().split()))
p = permutations([0, 1, 2])
ans = 10**9
for pi in p:
    t0 = pi[0]
    t1 = pi[1]
    t2 = pi[2]
    tmp = abs(A[t1] - A[t0]) + abs(A[t2] - A[t1])
    ans = min(ans, tmp)
print(ans)
