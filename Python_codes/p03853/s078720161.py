H,W = map(int, input().split())
ab = [input() for i in range(H)]

res = [0 for i in range(H*2)]

for i in range(0,H):
    res[(i+1)*2-1] = ab[i]
    res[(i)*2] = ab[i]

for j in range(0,H*2):
    print(res[j])