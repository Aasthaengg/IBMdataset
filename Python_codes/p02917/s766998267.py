n = int(input())
b = list(map(int,input().split()))
a = [0]*n
a[0] = b[0]
a[n-1] = b[n-2]
if n >= 3:
    for i in range(2,n):
        a[i-1] = min(b[i-1],b[i-2])
print(sum(a))