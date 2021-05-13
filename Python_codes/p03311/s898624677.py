
n = int(input())
a = list(map(int,input().split()))

for i in range(1,n+1):
    a[i-1] = a[i-1]-i

a.sort()
if n%2 == 1:
    b = a[n//2]
else:
    b = (a[n//2-1]+a[n//2])//2

total = 0
for i in range(n):
    total +=abs(a[i]-b)

print(total)