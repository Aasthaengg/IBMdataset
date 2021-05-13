# -*- coding: utf-8 -*-
#E - Friendships
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int,readline().split())
if K > (N-1)*(N-2)//2:
    print(-1)
else:
    # Nを頂点とするスターグラフを考える
    ans = []
    for i in range(1,N):
        ans.append((i,N))
    M = N*(N-1)//2 - K
    cnt = N-1
    flag = False
    for i in range(1,N):
        for j in range(i+1,N):
            if cnt == M:
                flag = True
                break
            ans.append((i,j))
            cnt += 1
        if flag:
            break
    print(M)
    for x,y in ans:
        print(x,y)