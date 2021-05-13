n=int(input())
a=[[int(i) for i in input().split()] for _ in range(n)]
u=0
for x in a[::-1]:
    if (x[0]+u)%x[1]!=0:u+=((x[0]+u)//x[1]+1)*x[1]-x[0]-u
print(u)