N, K = map(int, input().split())
S = [False]*N

for _ in range(K):
    d = int(input())
    A = map(int, input().split())
    for x in A:
        S[x-1] = True

print(sum(1 for x in S if not x))
