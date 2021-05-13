k,n = map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,a[n-1]-k)
l = 0
for z in range(n):
    b = a[z+1] - a[z] 
    if b > l:
        l = b
print(k-l)