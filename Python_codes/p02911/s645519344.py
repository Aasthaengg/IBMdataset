n,k,q=map(int,input().split())
a=[0 for i in range(n+1)]
for i in range(q):
    a[int(input())]+=1
for i in range(1,n+1):
    if q-a[i]<k:
        print("Yes")
    else:
        print("No")
        
