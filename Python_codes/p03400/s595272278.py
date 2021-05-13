n=int(input())
d,x=map(int,input().split())
a=[int(input())for i in range(n)]
res=x+n
for i in range(n):
    res+=(d-1)//a[i]
print(res)