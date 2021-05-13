n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
count = b[a[0]-1]
for i in range(1,n):
    if a[i] - a[i-1] == 1:
        count += b[a[i]-1] + c[a[i-1]-1]
    else:
        count += b[a[i]-1]
print(count)