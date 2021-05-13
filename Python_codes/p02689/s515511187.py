N, M = map(int, input().split())
H = [int(x) for x in input().split()]

d = [1] * N

for i in range(M):
    A, B = map(int, input().split())
    if H[A - 1] >= H[B - 1]:
        d[B - 1] = 0
    if H[A - 1] <= H[B - 1]:
        d[A - 1] = 0


print(sum(d))
