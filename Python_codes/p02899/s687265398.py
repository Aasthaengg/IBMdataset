a=int(input())
b=list(map(int,input().split()))

c=list(range(1,a+1))
d=[]
for i in range(a):
    d.append([c[i],b[i]])
d.sort(key=lambda x: x[1])
ans=[]
for i in range(a):
    ans.append(d[i][0])
print(' '.join(map(str,ans)))