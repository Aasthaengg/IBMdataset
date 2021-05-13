N, K = map(int, input().split())
data = [int(i) for i in input().split()]
D = sorted(data, reverse=True)
ma = 0

for i in range(K):
    ma += D[i]

print(ma)