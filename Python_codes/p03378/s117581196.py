n,m,x=map(int,input().split())
a=list(map(int,input().split()))
up,down=0,0
for i in range(m):
    if a[i]>x:
        up+=1
    else:
        down+=1
print(min(up,down))