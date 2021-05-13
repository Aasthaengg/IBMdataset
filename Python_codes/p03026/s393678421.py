from collections import deque

n = int(input())
V = [[] for i in range(n+1)]

a = [0]*(n-1)
for i in range(n-1):
    A,B = map(int,input().split())
    V[A].append(B)
    V[B].append(A)

c = list(map(int,input().split()))
c = sorted(c, reverse=True)
ans = sum(c[1:])


L = [0]*n
for i in range(1,n+1):
    L[i-1] = [i, len(V[i])]
    
L.sort(key= lambda val : val[1], reverse=True)

q = deque([])
d = [-1] + [0]*n
j = 0

q.append(L[0][0])
d[L[0][0]] = c[0]
j += 1

while q:
    x = q.popleft()
    for y in V[x]:
        if d[y] <= 0:
            q.append(y)
            d[y] = c[j]
            j += 1

print(ans)
for i in range(1,n+1):
    print(d[i],end="")
    print(" ",end="")