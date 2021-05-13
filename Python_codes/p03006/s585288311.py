# coding: utf-8
# Your code here!
N=int(input())

l=[]
for i in range(N):
    l.append(list(map(int,input().split())))

dis=[[0]*(N) for i in range(N-1)]
#print(dis)

for i in range(N-1):
    for j in range(i+1,N):
        if l[i][0]-l[j][0]>0:
            dis[i][j]=[(l[i][0]-l[j][0]),(l[i][1]-l[j][1])]
        elif l[i][0]-l[j][0]<0:
            dis[i][j]=[-(l[i][0]-l[j][0]),-(l[i][1]-l[j][1])]
        else:
            dis[i][j]=[(l[i][0]-l[j][0]),abs(l[i][1]-l[j][1])]

temp=0
for i in range(N-1):
    for item in dis[i]:
        if item!=0:
            temp=max(sum(x.count(item) for x in dis),temp)

#print(l)
#print(dis)
print(N-temp)

