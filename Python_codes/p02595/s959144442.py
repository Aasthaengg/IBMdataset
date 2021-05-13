N,D = map(int,input().split())
l =[list(map(int,input().split())) for i in range(N)] 
c = 0
for i in range(N):
    if (l[i][0]**2+l[i][1]**2)**0.5<=D:
        c+=1
    else:
        pass
print(c)