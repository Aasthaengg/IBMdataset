import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

H,W = map(int,input().split())
S = [input().rstrip() for _ in range(H)]
ans = 0
for hi in range(H):
    for wi in range(W):
        flag = 0
        if S[hi][wi] =='.':
            flag = 1
            tmp = [hi,wi]
    
            cost = [[-1]*W for _ in range(H)]
            q = collections.deque([tmp])
            cost[tmp[0]][tmp[1]] = 0
            while q:
                now = q.popleft()
                if 0<= now[0]+1 < H:
                    if cost[now[0]+1][now[1]] == -1 and S[now[0]+1][now[1]] =='.':
                        cost[now[0]+1][now[1]] = cost[now[0]][now[1]] +1
                        q.append([now[0]+1,now[1]])

                if 0<= now[0]-1 < H:
                    if cost[now[0]-1][now[1]] == -1 and S[now[0]-1][now[1]] =='.':
                        cost[now[0]-1][now[1]] = cost[now[0]][now[1]] +1
                        q.append([now[0]-1,now[1]])

                if 0<=now[1]+1 < W:
                    if cost[now[0]][now[1]+1] == -1 and S[now[0]][now[1]+1] =='.':
                        cost[now[0]][now[1]+1] = cost[now[0]][now[1]] +1
                        q.append([now[0],now[1]+1])

                if 0<=now[1]-1 < W:
                    if cost[now[0]][now[1]-1] == -1 and S[now[0]][now[1]-1] =='.':
                        cost[now[0]][now[1]-1] = cost[now[0]][now[1]] +1
                        q.append([now[0],now[1]-1])

            ans = max(ans,cost[now[0]][now[1]])

            cost = [[-1]*W for _ in range(H)]
            q = collections.deque([tmp])
            cost[now[0]][now[1]] = 0
            while q:
                now = q.popleft()
                if 0<= now[0]+1 < H:
                    if cost[now[0]+1][now[1]] == -1 and S[now[0]+1][now[1]] =='.':
                        cost[now[0]+1][now[1]] = cost[now[0]][now[1]] +1
                        q.append([now[0]+1,now[1]])

                if 0<= now[0]-1 < H:
                    if cost[now[0]-1][now[1]] == -1 and S[now[0]-1][now[1]] =='.':
                        cost[now[0]-1][now[1]] = cost[now[0]][now[1]] +1
                        q.append([now[0]-1,now[1]])

                if 0<=now[1]+1 < W:
                    if cost[now[0]][now[1]+1] == -1 and S[now[0]][now[1]+1] =='.':
                        cost[now[0]][now[1]+1] = cost[now[0]][now[1]] +1
                        q.append([now[0],now[1]+1])

                if 0<=now[1]-1 < W:
                    if cost[now[0]][now[1]-1] == -1 and S[now[0]][now[1]-1] =='.':
                        cost[now[0]][now[1]-1] = cost[now[0]][now[1]] +1
                        q.append([now[0],now[1]-1])
            
    if flag == 1:
        ans = max(ans,cost[now[0]][now[1]])
        
print(ans)

