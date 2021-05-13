from bisect import bisect_left
n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
d=[0]
e=[]
for i in range(n):
    d.append(bisect_left(a,b[i])+d[-1])
    e.append(bisect_left(b,c[i]))
ans=0
for i in e:
    ans+=d[i]
print(ans)