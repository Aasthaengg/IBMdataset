import itertools
n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
c=itertools.combinations(range(n),2)
d=itertools.combinations(range(n),2)
ans=10**25
for i0 in range(n):
    for i1 in range(i0,n):
        for j0 in range(n):
            for j1 in range(j0,n):
                i=[i0,i1]
                j=[j0,j1]
                #print(i,j)
                lx=min(l[i[0]][0],l[i[1]][0])
                rx=max(l[i[0]][0],l[i[1]][0])
                dy=min(l[j[0]][1],l[j[1]][1])
                uy=max(l[j[0]][1],l[j[1]][1])
                tk=0
                for p in l:
                    if lx<=p[0]<=rx and dy<=p[1]<=uy:
                        tk+=1
                if tk>=k:
                    ans=min(ans,(uy-dy)*(rx-lx))
print(ans)
