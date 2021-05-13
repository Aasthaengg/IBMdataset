N,x=map(int,input().split())
a=list(map(int,input().split()))

a.sort()

Q=0
for i in range(N):
    if x>=a[i] and i!=N-1:
        Q+=1
        x=x-a[i]
    elif i==N-1 and x==a[i]:
        Q+=1
print(Q)