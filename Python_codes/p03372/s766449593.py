n,c = map(int,input().split())
xv = [[int(i) for i in input().split()] for j in range(n)]

jun1 = [0]*n
jun2 = [0]*n

rev1 = [0]*n
rev2 = [0]*n

tmpj = 0
oldj = 0

tmpr = 0
oldr = 0

rv = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    rv[i][0] = c - xv[n-1-i][0]
    rv[i][1] = xv[n-1-i][1]

for i in range(n):
    #old += xv[i][1]
    tj = xv[i][1] - (xv[i][0]-oldj)
    tmpj += tj
    oldj = xv[i][0]
    jun1[i] = tmpj
    
    
    tr = rv[i][1] - (rv[i][0]-oldr)
    tmpr += tr
    oldr = rv[i][0]
    rev1[i] = tmpr

tmpj = 0
oldj = 0

tmpr = 0
oldr = 0
   
for i in range(n):
    tj = xv[i][1] - (xv[i][0]-oldj)*2
    tmpj += tj
    oldj = xv[i][0]
    jun2[i] = tmpj
    
    tr = rv[i][1] - (rv[i][0]-oldr)*2
    tmpr += tr
    oldr = rv[i][0]
    rev2[i] = tmpr
    
tmp = 0    
for i in range(n):
    tmp = max(tmp,jun2[i])
    jun2[i] = tmp
    
tmp = 0
for i in range(n):
    tmp = max(tmp,rev2[i])
    rev2[i] = tmp

#print(jun2,rev1,rev2,jun1)
ans = 0

for i in range(n):
    if i == n-1:
        ans = max(ans,jun1[i],rev1[i])
        break
    ans = max(max(0,jun1[i])+rev2[n-i-2],ans)
    ans = max(max(0,rev1[i])+jun2[n-i-2],ans)

print(ans)