n=int(input())
d=[list(map(int,input().split())) for _ in range(n)]

ans=cnt=0
for i in range(n-1):
  for j in range(i+1,n):
    ans+=((d[i][0]-d[j][0])**2+(d[i][1]-d[j][1])**2)**0.5
print(2*ans/n)
