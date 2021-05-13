from collections import deque
N, X, Y = map(int, input().split())
cnt_l = [0]*N

def bfs(start):
    d = deque()
    d.append(start)
    step_cnts = [-1]*(N+1)
    step_cnts[start] = 0
    while(d):
        i = d.popleft()
        cnt = step_cnts[i]
        if(i==X):
            next = (i-1, Y, i+1)
        elif (i==Y):
            next = (i-1, X, i+1)
        else:
            next = (i-1, i+1)
        cnt += 1
        for j in next:
            if(j<1 or N<j):
                continue
            if(step_cnts[j]!=-1):
                continue
            d.append(j)
            step_cnts[j] = cnt
            cnt_l[cnt] += 1

for i in range(1, N+1):
    bfs(i)

for i in range(1, N):
    print(cnt_l[i]//2)
