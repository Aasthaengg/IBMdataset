import sys
input = sys.stdin.readline

H,W = list(map(int,input().split()))
cell = []
for i in range(H):
    s = list(input().rstrip())
    cell.append(s)
for ih in range(H):
    for iw in range(W):
        if cell[ih][iw] == '.':
            ans =0
            for iih in range(max(0,ih-1),min(ih+2,H)):
                for iiw in range(max(0,iw-1),min(iw+2,W)):
                    if cell[iih][iiw]=='#':
                        ans+=1
            cell[ih][iw] = ans
for i in range(H):
    for j in range(W):
        print(cell[i][j],end='')
    print('')