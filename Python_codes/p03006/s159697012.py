n = int(input())
INF = 114514191981036436433-4
xy = []
for i in range(n):
    x,y = map(int,input().split())
    xy.append((x,y))
    
a = n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
            
        p,q = xy[i][0] - xy[j][0] , xy[i][1] - xy[j][1]
        ans = n
        
        for k in range(n):
            for l in range(n):
                xx,yy = xy[k][0] - xy[l][0] , xy[k][1] - xy[l][1]
                if xx == p and yy == q:
                    ans -= 1
                    
        a = min(a,ans)
        
print(a)