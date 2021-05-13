n,k,q=map(int,input().split())
p=[0 for i in range(n)]
if k>q:
    for i in range(n):
        print("Yes")
else:
    for i in range(q):
        a=int(input())
        p[a-1]+=1
    for i in p:
        if i<q-k+1:
            print("No")
        else:
            print("Yes")
