from collections import deque
import copy
H,W= map(int, input().split())
c=[list(input()) for i in range(H)]

max_num=0
move=[[0,1],[0,-1],[1,0],[-1,0]]
for h in range(H):
    for w in range(W):
        if c[h][w]=='.':
            #初期位置#(H,W)
            L=copy.deepcopy(c)
            d=deque([[h,w]])
            L[h][w]='S'

            num=0
            while d:
                num+=1
                for i in range(len(d)):
                    q=d.popleft()
                    for m in move:
                        if 0<=q[0]+m[0]<=H-1 and 0<=q[1]+m[1]<=W-1 and L[q[0]+m[0]][q[1]+m[1]]=='.':
                            L[q[0]+m[0]][q[1]+m[1]]=num

                            d.append([q[0]+m[0],q[1]+m[1]])

           # print(num-1)
            if num-1>=max_num:
                max_num=num-1
print(max_num)