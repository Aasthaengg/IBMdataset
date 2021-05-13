k=int(input())
n=50

a=[k//n+49 for i in range(n)]

for i in range(n):
    if i<k%n:
        a[i]+=n-k%n+1
    else:
        a[i]-=k%n

print(n)
for i in range(n):
    if i<n-1:
        print(a[i],end=" ")
    else:
        print(a[i])
    




