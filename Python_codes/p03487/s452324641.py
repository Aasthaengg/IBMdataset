n=int(input())
a=list(map(int,input().split()))
b=[0]*(n+2)
for i in range(n):
    if a[i]>n:
        b[n+1]+=1
    else:
        b[a[i]]+=1
sm=0
for i in range(1,n+1):
    if b[i]>i:
        sm+=b[i]-i
    elif b[i]<i:
        sm+=b[i]

sm+=b[n+1]
print(sm)
