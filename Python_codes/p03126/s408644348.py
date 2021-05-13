N,M = map(int, input().split())

ans = set(range(1, M+1))

for _ in range(N):
    L = list(map(int, input().split()))
    ans &= set(L[1:])

print(len(ans))