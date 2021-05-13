N, H, W = map(int, input().split())
ab = [[int(i) for i in input().split()] for i in range(N)] 
k = 0
for x in ab:
    if x[0] >= H and x[1] >= W:
        k += 1
    else: pass
print(k)