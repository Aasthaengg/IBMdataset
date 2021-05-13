N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

lst = [0]*(N+1)

for i in range(N):
    ref = S[i]
    lst[i] = S.count(ref) - T.count(ref)

ans = max(lst)
print(ans)
