from collections import defaultdict

H, W, N = map(int, input().split())

mem = defaultdict(int)
for _ in range(N) :
    a, b = map(int, input().split())
    for i in range(max(1, a-1), min(H, a+1)+1) :
        for j in range(max(1, b-1), min(W, b+1)+1) :
            mem[(i, j)] += 1
            
ret = [0] * 10
for k, v in mem.items() :
    if 2 <= k[0] <= H - 1 and 2 <= k[1] <= W - 1 :
        ret[v] += 1

ret[0] = (H - 2) * (W - 2) - sum(ret)
 
for r in ret :
    print(r)
