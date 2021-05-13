#prdさんのを写経
import sys
input=sys.stdin.readline

n=int(input())
a=[list(reversed(list(map(lambda x:int(x)-1, input().split())))) for _ in range(n)]
b={i:r for i,r in enumerate(a)}

end=0
for k in range(8000):
    used=set()
    dels=[]
    for i,q in b.items():
        if not q:
            continue
        if i in used:
            continue
        j=q[-1]
        if j in used:
            continue
        if a[j][-1]==i:
            a[j].pop()
            a[i].pop()
            used.add(i)
            used.add(j)
            if not a[i]:
                end+=1
                dels.append(i)
            if not a[j]:
                end+=1
                dels.append(j)
    if not used:
        print(-1)
        exit()
    if end==n:
        print(k+1)
        exit()
    for i in dels:
        del b[i]

print(n*(n-1)//2)
