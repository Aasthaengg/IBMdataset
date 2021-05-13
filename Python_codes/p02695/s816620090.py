from itertools import combinations_with_replacement
ans = 0
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]
for A in combinations_with_replacement(range(1, M+1), N):
    tmp = 0
    for i in range(Q):
        a,b,c,d = abcd[i]
        a-=1
        b-=1
        if A[b]-A[a] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)