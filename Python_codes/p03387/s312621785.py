a = list(map(int,input().split()))
a = sorted(a)
i = (a[1] - a[0])//2
a[0] += i*2
i += a[2] - a[1]
if a[0] != a[1]:
  i += 2

print(i)
  
  
