import sys


H,W,K = [int(_) for _ in input().split()]
l = []
c = 0
if W == 1:
    print(1)
    sys.exit()
#0本
l.append([0 for _ in range(W-1)])
#1本
for i in range(0, W-1):
    a = [0 for _ in range(W-1)]
    for j in range(0, W-1):
        if j == i:
            a[j] = 1
        else:
            a[j] = 0
    l.append(a)
#2本
if W >= 4:
    for i in range(0, W-3):
        for j in range(i+2, W-1):
            a = [0 for _ in range(W-1)]
            for k in range(0, W-1):
                if k == i or k == j:
                    a[k] = 1
                else:
                    a[k] = 0
            l.append(a)
#3本
if W >= 6:
    for i in range(0, W-5):
        for j in range(i+2, W-3):
            for k in range(j+2, W-1):
                a = [0 for _ in range(W-1)]
                for p in range(W-1):
                    if p == i or p == j or p == k:
                        a[p] = 1
                    else:
                        a[p] = 0
                l.append(a)
#4本
if W == 8:
    l.append([1,0,1,0,1,0,1])


HW = [[0 for _ in range(W)] for _ in range(H+1)]
HW[0][0] = 1

for i in range(0, H):
    for j in range(0,W):
        for k in range(len(l)):
            q = HW[i][j]
            if j == 0:
                if l[k][j] == 1:
                    HW[i+1][j+1] += q
                else:
                    HW[i+1][j] += q
            elif j == W-1:
                if l[k][j-1] == 1:
                    HW[i+1][j-1] += q
                else:
                    HW[i+1][j] += q
            else:
                if l[k][j] == 0 and l[k][j-1] == 0:
                    HW[i+1][j] += q
                elif l[k][j] == 1:
                    HW[i+1][j+1] += q
                else:
                    HW[i+1][j-1] += q
        for x in range(0, W):
            HW[i+1][x] = HW[i+1][x] % 1000000007
  
ans = HW[H][K-1]

print(ans)
