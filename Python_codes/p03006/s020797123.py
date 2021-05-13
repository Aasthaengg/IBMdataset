n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
d=[]
if n==1:
    print(1)
else:
    for i in range(n):
        for j in range(n):
            if i!=j:
                d.append([xy[i][0]-xy[j][0],xy[i][1]-xy[j][1]])
    d.sort()
    res = 1
    tres = 1
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            tres += 1
        else:
            tres = 1
        res = max(res,tres)
    print(n-res)