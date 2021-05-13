N = int(input())
e_list = [[] for i in range(N)]
for i in range(N-1):
        a,b = list(map(int,input().split()))
        a,b = a-1,b-1
        e_list[a].append(b)
        e_list[b].append(a)
c = list(map(int,input().split()))

vi = 0 #時と場合によってここを変える
from collections import deque
Q = deque([vi])
checked_list = [False for i in range(N)]
checked_list[vi]=True
min_path_list = [10**27 for i in range(N)] #問題によりここを変える
min_path_list[vi] = 0
while len(Q)>0:
    v = Q.pop()
    for v1 in e_list[v]:
        if not checked_list[v1]:
            checked_list[v1]=True
            Q.appendleft(v1)
            min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1) #問題によりここを変える


min_i_list = [[i,min_path_list[i]] for i in range(N)]
min_i_list.sort(key=lambda x:x[1],reverse=True)

c.sort()

ans = [[min_i_list[i][0]+1, c[i]] for i in range(N)]

ans.sort(key=lambda x:x[0])
ans = [ans[i][1] for i in range(N)]
print(sum(c[:-1]))
print(*ans)