n = int(input())
a = list(map(int, input().split()))

if n%2 != 0:
  a.append(0)
  n += 1
 
a.sort()
d = 0

for i in range(int(n/2)):
               d += a[2*i+1]-a[2*i]
           
print(d)
