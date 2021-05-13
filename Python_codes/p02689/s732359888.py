import collections
N, M = map(int, input().split())
H = [0]
H += list(map(int, input().split()))

a_l = [1] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    if H[a] > H[b]:
        a_l[b] = 0
    elif H[a] < H[b]:
        a_l[a] = 0
    else:
        a_l[a] = a_l[b] = 0
print(a_l.count(1) - 1)