n=int(input())
ta=[list(map(int,input().split())) for i in range(n)]
a,b=1,1
for i in range(n):
  l=-min(-a//ta[i][0],-b//ta[i][1])
  a=ta[i][0]*l
  b=ta[i][1]*l
print(a+b)