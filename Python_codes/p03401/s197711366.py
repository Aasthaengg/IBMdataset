n = int(input())
a = [int(i) for i in input().split()]

tmp = abs(a[0])

for i in range(1,n):
  tmp += abs(a[i] - a[i-1])
  
tmp += abs(a[-1])
a = [0] + a + [0]

for i in range(1,n+1):
  print(tmp - (abs(a[i] - a[i - 1])) - (abs(a[i] - a[i+1])) + abs(a[i-1] - a[i+1]))
    
