n,q=map(int,input().split())
s=list(input())
l=[0 for i in range(n+1)]
tmp=0
for i in range(1,n):
    if s[i]=="C" and s[i-1]=="A":
        tmp+=1
    l[i]=tmp
for i in range(q):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    print(l[b]-l[a])