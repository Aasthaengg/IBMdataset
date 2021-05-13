n=int(input())
city=[list(map(int,input().split())) for _ in range(n)]
length=[]
for i in range(n-1):
    for j in range(i+1,n):
        len=((city[i][0]-city[j][0])**2+(city[i][1]-city[j][1])**2)
        length.append(len**(0.5))
ans=sum(length)*2/n
print("{:.7f}".format(ans))