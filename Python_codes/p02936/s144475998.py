import sys
sys.setrecursionlimit(2*10**9)

N,Q=map(int, input().split())

adj_list = [[] for _ in range(N)]
counter = [0 for _ in range(N)]
reached = [0 for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    adj_list[a].append(b)
    adj_list[b].append(a)

def df(current, score):
    next_nodes = adj_list[current]
    reached[current]=1
    for node in next_nodes:
        if reached[node]==0:
            counter[node]+=score
            df(node, counter[node])

for _ in range(Q):
    p,x=map(int, input().split())
    counter[p-1]+=x
df(0, counter[0])
print(*counter)
