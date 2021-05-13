A, B, C = map(int, input().split())
K = int(input())
for _ in range(K):
    if A == max(A, B, C):
        A *= 2
    elif B == max(A, B, C):
        B *= 2
    else:
        C *= 2
print(sum([A, B, C]))
