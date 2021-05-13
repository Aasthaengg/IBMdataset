import sys,math,collections,itertools,copy
input = sys.stdin.readline

H,W=list(map(int,input().split()))
s = []
dot_cnt = 0
for _ in range(H):
    a = input().rstrip()
    dot_cnt += a.count('.')
    s.append(list(a))

num_lis = [[float('inf')]*W for _ in range(H)]

#--#
for ih in range(H):
    for iw in range(W):
        if s[ih][iw]=='#':
            num_lis[ih][iw]=0
        else:
            if iw-1>=0:
                num_lis[ih][iw] = min(num_lis[ih][iw-1]+1,num_lis[ih][iw])
                
    for iw in range(W-1,-1,-1):
        
        if s[ih][iw]=='#':
            num_lis[ih][iw]=0
        else:
            if iw+1<=W-1:
                num_lis[ih][iw] = min(num_lis[ih][iw+1]+1,num_lis[ih][iw])

#--#
for iw in range(W):
    for ih in range(H):
        if s[ih][iw]=='#':
            num_lis[ih][iw]=0
        else:
            if ih-1>=0:
                num_lis[ih][iw] = min(num_lis[ih-1][iw]+1,num_lis[ih][iw])
                
    for ih in range(H-1,-1,-1):
        if s[ih][iw]=='#':
            num_lis[ih][iw]=0
        else:
            if ih+1<=H-1:
                num_lis[ih][iw] = min(num_lis[ih+1][iw]+1,num_lis[ih][iw])

maxOpe = 0
for iw in range(W):
    for ih in range(H):
        maxOpe = max(maxOpe,num_lis[ih][iw])
print(maxOpe)
