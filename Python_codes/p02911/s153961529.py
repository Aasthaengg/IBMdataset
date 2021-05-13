n,k,q=map(int,input().split())
l=[0]*(n+1)
for i in range(q):
    a=int(input())
    l[a]+=1
for i in range(1,n+1):
    if l[i]>q-k:
        print("Yes")
    else:
        print("No")