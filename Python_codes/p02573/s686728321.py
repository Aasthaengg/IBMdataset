from collections import *
N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(M)]

lst=[[] for i in range(N+1)]

for a,b in AB:
    lst[a].append(b)
    lst[b].append(a)



used=set(list(range(1,N+1)))
value=-10**18
while used:
    a=used.pop()
    stack=[a]

    visited={a}
    while stack:
        a=stack.pop()
        for p in lst[a]:
            if p in used:
                used.remove(p)
            if not p in visited:
                visited.add(p)
                stack.append(p)
    value=max(len(visited),value)
print(value)
