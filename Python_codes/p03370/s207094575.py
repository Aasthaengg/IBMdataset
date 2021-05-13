n,x=map(int,input().split())
l=[0]*n
for i in range(n):
    l[i]=int(input())
print(n+(x-sum(l))//min(l))