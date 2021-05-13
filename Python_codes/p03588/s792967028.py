n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
y=0
z=0
for i in x:
    a,b=i[0],i[1]
    if y<a:
      y=a
      z=b
print(y+z)