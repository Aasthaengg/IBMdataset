import bisect

n,m=map(int,input().split())

x=[list(map(int,input().split())) for i in range(m)]

lst=[[] for i in range(n)]

for i,v in x:
    lst[i-1].append(v)

for i in range(n):
    lst[i].sort()

for i,v in x:
    z=bisect.bisect_left(lst[i-1],v)+1

    print('0'*(6-len(str(i)))+str(i)+'0'*(6-len(str(z)))+str(z))