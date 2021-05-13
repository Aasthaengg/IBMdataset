import sys,math,collections,itertools
input = sys.stdin.readline

H,W = list(map(int,input().split()))
s = [input().rstrip() for _ in range(H)]
maperW = [[0]*W for _ in range(H)]
maperH = [[0]*W for _ in range(H)]


#--W方向を調べる--#
for ih in range(H):
    for iw in range(W):
        if s[ih][iw]=='#':
            maperW[ih][iw]=0
        elif s[ih][iw]=='.' and iw == 0:
            maperW[ih][iw]=1
        else:
            maperW[ih][iw]=1+maperW[ih][iw-1]
    for iw in range(W-2,-1,-1):
        if maperW[ih][iw+1] == 0 or maperW[ih][iw]==0:
            continue
        else:
            maperW[ih][iw] = maperW[ih][iw+1]
#--H方向を調べる--#
for iw in range(W):
    for ih in range(H):
        if s[ih][iw]=='#':
            maperH[ih][iw]=0
        elif s[ih][iw]=='.' and ih == 0:
            maperH[ih][iw]=1
        else:
            maperH[ih][iw]=1+maperH[ih-1][iw]
    for ih in range(H-2,-1,-1):
        if maperH[ih+1][iw] == 0 or maperH[ih][iw]==0:
            continue
        else:
            maperH[ih][iw] = maperH[ih+1][iw]
ans = 0
for iw in range(W):
    for ih in range(H):
        ans = max(ans,maperW[ih][iw]+maperH[ih][iw]-1)
print(ans)
