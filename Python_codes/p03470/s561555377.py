N = int(input())
a=[0]*N
count=1

for i in range(N):
    a[i]=int(input())
a.sort()
for i in range(N-1):
    if a[i] != a[i+1]:
        count = count + 1
print(count)
