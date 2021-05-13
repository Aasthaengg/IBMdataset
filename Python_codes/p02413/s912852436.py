H, W = map(int, raw_input().split())
HW = [[0 for i in range(W+1)] for j in range(H+1)]
for i in range(H):
    tmp = map(int, raw_input().split())
    for j in range(W):
        HW[i][j] = tmp[j]
    HW[i][W] = sum(HW[i])
for i in range(W+1):
    tmp = 0
    for j in range(H):
        tmp+=HW[j][i]
    HW[H][i] = tmp
        
    
for i in range(H+1):
    print " ".join(map(str, HW[i]))
