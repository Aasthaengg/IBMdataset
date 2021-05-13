n=int(input())
d,x=map(int,input().split())
a=[int(input())for i in range(n)]
res=x
for i in range(n):
    for j in range(d):
        if j%a[i]==0:
            res+=1
print(res)