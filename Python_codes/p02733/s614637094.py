# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
H, W, K = map(int, readline().split())
S = [readline().decode().rstrip() for _ in range(H)]
INF = 10**30
data = [[0]*W for _ in range(H)]
for i in range(H):
    cnt = 0 
    for j in range(W):
        if S[i][j] == '1':
            data[i][j] += 1

ans_cnt = INF   
for bit_H in range(1 << (H-1)):
    cnt = 0
    ans = []
    new_data = []
    for i in range(H-1):
        if (bit_H >> i) & 1:
            ans.append(i)
    ans.append(H-1)
    tmp = [0]*W
    for i in range(H):
        for j in range(W):
            tmp[j] += data[i][j]
        if i in ans:
            new_data.append(tmp)
            tmp = [0]*W
    group = len(new_data)
    cnt += group-1
    white = [0] * group
    flag = True
    for i in range(W):
        diff = [0] * group
        for j in range(group):
            diff[j] += new_data[j][i]
            white[j] += new_data[j][i]
        max_diff = max(diff)
        if max_diff > K:
            flag = False
            break
        max_white = max(white)
        if max_white > K:
            cnt +=1
            white = diff[:]
    if flag:
        ans_cnt = min(ans_cnt,cnt)
print(ans_cnt)
    
