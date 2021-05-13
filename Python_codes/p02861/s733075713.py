n=int(input())
P=[list(map(int,input().split())) for i in range(n)]
dist=0
for i in range(n-1):
    for j in range(i+1,n):
        dist+=((P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2)**0.5
print(2*dist/n)
