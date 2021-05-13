n = int(input())
a = list(map(int, input().split()))

b = [0]*n
c = [0]*(n-1)
for i in range(n-1):
  c[i] += a[i]-b[i]
  b[i+1] += c[i]

first = (a[-1] - b[-1])//2
b = [0]*n
b[0] = first
c = [0]*(n-1)
for i in range(n-1):
  c[i] += a[i]-b[i]
  b[i+1] += c[i]

print(int(first*2), end = " ")
for i in range(len(c)):
  print(int(c[i]*2), end = " ")