h,w = map(int,input().split())
L = [[]*w for i in range(h)]

for i in range(h):
    L[i] = list("#" + input() + "#")
L = [["#" for i in range(w+2)]] + L + [["#" for i in range(w+2)]]
#print(L)

from collections import deque
ans = 0
q = deque([])
for j in range(1,h+1):
    for i in range(1,w+1):
        cost = [[-1]*(w+2) for i in range(h+2)]
        li = ((1,0),(0,1),(-1,0),(0,-1))
        #print(j,i)
        if L[j][i] == ".":
            cost[j][i] = 0
        cost_max = 0
        q.append((j,i))
        while q:
            #print(q)
            r,s = q.popleft()
            
            for dh,dw in li:
                nh,nw = r+dh,s+dw
                #print(L[nh][nw],)
                if L[nh][nw] =="." and cost[nh][nw] == -1 :
                    cost[nh][nw] = cost[r][s] + 1
                    #print(cost[nh][nw],cost[j][i])
                    #print(cost)
                    cost_max = max(cost_max,cost[nh][nw])
                    q.append((nh,nw))
        ans = max(ans,cost_max)
print(ans)