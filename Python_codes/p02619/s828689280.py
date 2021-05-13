D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(D)]
t=[int(input()) for i in range(D)]
C=sum(c)
l=[0]*26
a=0
m=0
for i in range(D):
    b=t[i]-1
    m+=C-c[b]*(i-l[b]+1)
    a+=s[i][b]-m
    l[b]=i+1
    print(a)