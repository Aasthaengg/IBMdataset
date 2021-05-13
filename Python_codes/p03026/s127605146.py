from collections import deque

N = int(input())
ki = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)
#print(ki)
c = list(map(int,input().split()))
c.sort()
c.reverse()
point = 1
lis = [0] * N
que = deque([0])
lis[0] = c[0]
while len(que) != 0:
    p = que.popleft()
    #print(p)
    for i in ki[p]:
        if lis[i] == 0:
            que.append(i)
            lis[i] = c[point]
            point += 1
print(sum(c)-c[0])
print(' '.join(map(str,lis)))
