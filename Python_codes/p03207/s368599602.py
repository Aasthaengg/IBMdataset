n = int(input())

a = [0]*n

for i in range(0,n):
  a[i] = int(input())
  
a.sort()
a[-1] = int(a[i]/2)
print(sum(a))