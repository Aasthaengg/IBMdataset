import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
lis = [[] for i in range(N)]
for i in range(N-1):
    a,b,w = map(int,input().split())
    lis[a-1].append((b-1,w%2))#移動先、偶奇の順
    lis[b-1].append((a-1,w%2))

flg = [True] * N
ans = [-1] * N
que = deque([ (0,0) ])
#flg[0] = False
ans[0] = 0
flg[0] = False
while len(que) != 0:
    p = que.popleft()
    #print(p)
    for i in lis[p[0]]:
        if flg[i[0]] == True:
            que.append(i)
            flg[i[0]] = False
            if i[1] == 0:
                ans[i[0]] = ans[p[0]]
            else:
                if ans[p[0]] == 1:
                    ans[i[0]] = 0
                else:
                    ans[i[0]] = 1
for i in ans:
    print(i)
