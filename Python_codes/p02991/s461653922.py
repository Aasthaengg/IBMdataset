import heapq
from collections import deque

N,M = map(int,input().split())

dic = {}

for i in range(M):

    u,v = map(int,input().split())
    u -= 1
    v -= 1

    if u not in dic:
        dic[u] = []

    dic[u].append(v)


far = [[float("inf")] * 3 for i in range(N)]
nend = [ [True] * 3 for i in range(N) ]

S,T = map(int,input().split())
S -= 1
T -= 1

q = deque([])
q.append([0,S])

while len(q) > 0:

    now = q.popleft()

    nd = now[0]
    np = now[1]
    nend[np][nd % 3] = False

    far[np][nd % 3] = min(far[np][nd % 3],nd)

    if np in dic:
        for i in dic[np]:

            if nend[i][(nd + 1) % 3] and far[i][(nd+1)%3] > far[np][nd%3] + 1:
                q.append([nd + 1 , i])
                nend[i][(nd+1)%3] = False

if far[T][0] == float("inf"):
    print (-1)
else:
    print (far[T][0] // 3)
    

