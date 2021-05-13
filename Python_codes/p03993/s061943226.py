n=int (input())
a= list(map(int, input().strip().split()))
count=0
for i in range(1,n+1):
    if a[a[i-1]-1]==i:
        count=count+1
print(count//2)