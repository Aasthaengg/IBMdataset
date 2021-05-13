from functools import reduce
n=int(input())
v=sorted([int(i)for i in input().split()])
x=lambda x,y:(x+y)/2
res=reduce(x,v)
print(res)