N, M = map(int, input().split())

KA = list(map(int, input().split()))
like = set(KA[1:])
for i in range(1, N):
    KA = list(map(int, input().split()))
    A = KA[1:]
    like = like & set(A)

print(len(like))
