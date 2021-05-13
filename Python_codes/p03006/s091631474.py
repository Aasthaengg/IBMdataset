n=int(input())
dic={}
d=[list(map(int,input().split())) for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if (d[i][0]-d[j][0],d[i][1]-d[j][1]) in dic:
            dic[(d[i][0]-d[j][0],d[i][1]-d[j][1])]+=1
            dic[(d[j][0]-d[i][0],d[j][1]-d[i][1])]+=1
        else:
            dic[(d[i][0]-d[j][0],d[i][1]-d[j][1])]=1
            dic[(d[j][0]-d[i][0],d[j][1]-d[i][1])]=1
ans=0
for i in dic.values():
    ans=max(ans,i)
print(n-ans)