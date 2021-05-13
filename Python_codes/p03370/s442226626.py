a,b=map(int,input().split())
c=[int(input()) for i in range(a)]
n=b-sum(c)
m=n//min(c)
print(a+m)