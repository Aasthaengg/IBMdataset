from bisect import bisect_left
n = int(input())
m=list(map(int,input().split()))
k=0
m.sort()
for i in range(n-2):
    for j in range(i+1,n-1):
        z=m[i]+m[j]
        l=bisect_left(m,z)
        k+=l-j-1
print(k)