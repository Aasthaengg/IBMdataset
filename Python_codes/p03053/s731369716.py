from collections import deque
import sys
input = sys.stdin.readline

H ,W = map(int, input().split())#↓H行数 →W列数
List = [list(str(input())) for i in range(H)]
#H=3
#W=3
#List=[['.', '.', '.'], ['.', '#', '.'], ['.', '.', '.']]
cheak=[['0' for i in range(W)] for j in range(H)]

q = deque([])

for h in range(H):
    for w in range(W):
        if List[h][w]=='#':
            cheak[h][w]='1'
            q.append([h,w])
#print(List)
#print(cheak)
move=[[1,0],[-1,0],[0,1],[0,-1]]
num=-1
#print(q)
while q:
    for rt in range(len(q)):
        i=q.popleft()
        for u in move:
            if 0<=i[0]+u[0]<=H-1 and 0<=i[1]+u[1]<=W-1 and cheak[i[0]+u[0]][i[1]+u[1]]=='0':
                q.append([i[0]+u[0],i[1]+u[1]])
                cheak[i[0]+u[0]][i[1]+u[1]]='1'
    #print(cheak)
    num+=1
print(num)  