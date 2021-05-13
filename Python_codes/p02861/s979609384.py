import itertools
n=int(input())
x=[]
y=[]
for i in range(n):
    x0, y0 = map(int,input().split())
    x.append(x0)
    y.append(y0)
    
ls = list(itertools.permutations(range(1,n+1)))

dist = 0
for i in ls:

    p0 = i[0]-1
    for j in range(1,len(i)):
        p1 = i[j]-1
        dist += ((x[p0]-x[p1])**2 + (y[p0]-y[p1])**2)**0.5
        p0=p1
        # print(dist)
    # print( )
        

print(dist/(len(ls)))
