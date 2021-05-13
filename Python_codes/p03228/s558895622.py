*a,k=map(int,input().split())
for i in range(k):
    a[1-i%2]+=a[i%2]//2
    a[i%2]=(a[i%2]-a[i%2]%2)//2
print(*a)