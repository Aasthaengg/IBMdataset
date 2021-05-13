N, M = map(int, input().split())
H = list(map(int,input().split()))

tmp = [1]*N

for m in range(M):
    a, b = map(int, input().split())

    if H[a-1] > H[b-1]:
        tmp[b-1] = 0
    elif H[a-1] < H[b-1]:
        tmp[a-1] = 0
    else:
        tmp[a-1] = 0
        tmp[b-1] = 0

print(sum(tmp))
