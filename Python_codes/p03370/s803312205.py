n,x=map(int,input().split())
m=[int(input()) for i in range(n)]
sum=sum(m)
min=min(m)
print(n+(x-sum)//min)