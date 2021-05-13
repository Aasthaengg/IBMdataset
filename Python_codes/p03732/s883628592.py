n,W = map(int,input().split())
lst = [[0]*(n+1) for _ in range(4)]
for i in range(n):
    w,v = map(int,input().split())
    if i == 0: x = w
    lst[w-x].append(v)
for i in range(4):
    lst[i].sort(reverse=True)
    for j in range(n): lst[i][j+1] += lst[i][j]
ans = 0
for a in range(n+1):
    for b in range(n+1-a):
        for c in range(n+1-a-b):
            if x*a+(x+1)*b+(x+2)*c > W: continue
            d = max((W-x*a-(x+1)*b-(x+2)*c)//(x+3),0)
            sumv = 0
            for i,j in enumerate((a,b,c,d)):
                if j == 0: continue
                sumv += lst[i][j-1]
            ans = max(sumv,ans)
print(ans)