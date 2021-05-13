n=int(input())
d=sorted([int(i)for i in input().split()])
res=d[n//2]-d[n//2-1]
print(res)