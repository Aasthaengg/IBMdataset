N, K = map(int,input().split())
H = sorted(list(map(int,input().split())))

for p in range(K):
    if N-p-1 >= 0:
        H[N-p-1] = 0

print(sum(H))