# coding: utf-8
# Your code here!
n=int(input())
a=list(map(int,input().split()))
w=int(input())
c=[]
for i in range(w):
    c.append(list(map(int,input().split())))

b=[0]*10**5
for i in range(n):
    b[a[i]-1]+=1
ans=sum(a)
for i in range(w):
    ans=ans+b[c[i][0]-1]*(c[i][1]-c[i][0])
    cnt=b[c[i][0]-1]
    b[c[i][1]-1]+=cnt
    b[c[i][0]-1]=0
    #print(b)
    print(ans)