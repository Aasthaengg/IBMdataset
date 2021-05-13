n,x,y=map(int,input().split())

c=min(x,y)-1
d=max(x,y)-1

e=[0]*n

for i in range(n):
    for j in range(i+1,n):
        a=j-i
        if i<c and d<j:
            b=c-i+j-d+1
        elif c<=i and d<j:
            b=i-c+j-d+1
        elif i<c and j<=d:
            b=c-i+d-j+1
        elif c<=i and j<=d:
            b=i-c+d-j+1
        t=min(a,b)
        #print(i,j,t)
        e[t]+=1
for f in e[1:]:
    print(f)