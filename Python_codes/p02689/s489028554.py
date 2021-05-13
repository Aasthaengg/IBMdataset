N, M = map(int, input().split())
H = list(map(int, input().split()))
yoi = [1] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if H[A] > H[B]:
        yoi[B] = 0
    elif H[B] > H[A]:
        yoi[A] = 0
    else:
        yoi[A] = 0
        yoi[B] = 0

print(sum(yoi))