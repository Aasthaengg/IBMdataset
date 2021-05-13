n=int(input())
l=list(map(int,input().split()))
d=list(map(int,input().split()))
c=0
for i in range(n):
    if(l[i]>d[i]):
        c+=l[i]-d[i]
print(c)