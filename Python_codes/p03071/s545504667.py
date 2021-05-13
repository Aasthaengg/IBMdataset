a,b=map(int,input().split())
num=0
c=max(a,b)
d=min(a,b)
num+=c
num+=max(c-1,d)
print(num)
