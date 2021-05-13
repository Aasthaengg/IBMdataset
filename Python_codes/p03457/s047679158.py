import sys
input = sys.stdin.buffer.readline #inputに置き換え可能

n = int(input())
txy = [[0,0,0]] + [list(map(int,input().split())) for i in range(n)]

flg = True
for i in range(1, n+1):
    dt = txy[i][0] - txy[i-1][0] 
    dx = abs(txy[i][1] - txy[i-1][1])
    dy = abs(txy[i][2] - txy[i-1][2])
    dxdy = dx + dy
    if dt % 2 != dxdy % 2 or dt < dxdy:
        flg = False
        break
print('Yes') if flg else print('No')