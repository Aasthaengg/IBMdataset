n,x=map(int,input().split())
m=[]
for i in range(n):
    m+=[int(input())]
res=(x-sum(m))//min(m)
print(res+n)