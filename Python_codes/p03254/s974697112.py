N,x = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

count = 0
total = 0
for i in range(N):
    total += a[i]
    if total <=x:
        count += 1
        
    else:
        break
if total < x:
    count = N-1
print(count)