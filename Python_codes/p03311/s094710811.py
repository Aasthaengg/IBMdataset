n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]-=i+1
b,c=sorted(a)[n//2],0
for i in range(n):
    c+=abs(a[i]-b)
print(c)