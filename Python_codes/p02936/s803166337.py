import queue

N, Q  = map(int,input().split())

ki = [[0,[]] for _ in range(N)]

for i in range(N-1):
    a,b  = map(int,input().split())
    a -= 1
    b -= 1
    ki[a][1].append(b)
    ki[b][1].append(a)

for i in range(Q):
    p,x = map(int,input().split())
    p -= 1
    ki[p][0] += x 

seen = [False for _ in range(N)]
que = queue.Queue()
que.put(0)
while not(que.empty()):
    now = que.get()
    seen[now] = True
    # print(ki[now][1])
    for i in range(len(ki[now][1])):
        nxt = ki[now][1][i]
        if seen[nxt]:
            continue
        else:
            ki[nxt][0] += ki[now][0]
            que.put(nxt)

for i in range(N):
    print("{} ".format(ki[i][0]),end="")
print()
