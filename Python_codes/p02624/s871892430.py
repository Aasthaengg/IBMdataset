n = int(input())
a = [0]*(n+1)
asum = 1

for i in range(2,n+1):
    a[i] += 1
    for k in range(i,n+1,i):
      a[k] += 1
    asum += i*a[i]
print(asum)