n=int(input())
List=[list(map(int,input().split())) for i in range(n)]
x=0
for i in range(n):
  x+=List[i][1]-List[i][0]+1
print(x)