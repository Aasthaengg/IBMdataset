from collections import deque
D1 = {i:chr(i+96) for i in range(1,27)}
D2 = {val:key for key,val in D1.items()}
N = int(input())
que = deque([("a",1)])
A = []
while que:
    x,n = que.popleft()
    if n<N:
        imax = 0
        for i in range(len(x)):
            imax = max(imax,D2[x[i]])
        for j in range(1,min(imax+1,26)+1):
            que.append((x+D1[j],n+1))
    else:
        A.append(x)
A = sorted(list(set(A)))
for i in range(len(A)):
    print(A[i])