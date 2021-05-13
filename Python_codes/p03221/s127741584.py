import bisect

n,m = map(int,input().split())

li = [[] for _ in range(n+1)]
num = []

for _ in range(m):
    p,y = map(int,input().split())
    li[p].append(y)
    num.append((p,y))

for i in range(n+1):
    li[i].sort()

for i,j in num:
    print(str(i).zfill(6)+str(bisect.bisect_left(li[i],j)+1).zfill(6))