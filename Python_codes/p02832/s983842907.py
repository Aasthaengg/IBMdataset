n=int(input())
a=[int(i) for i in input().split()]
d=1
c=0
for i in range(0,len(a)):
    if(a[i]==d):
        d=d+1
        c=c+1
if(c==0):
    print(-1)
else:
    print(len(a)-c)