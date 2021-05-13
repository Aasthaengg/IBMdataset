# Popular Vote
N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
ans = 0
for a in A:
    if a >= total/(4*M):
        ans += 1
print(['No','Yes'][ans >= M])