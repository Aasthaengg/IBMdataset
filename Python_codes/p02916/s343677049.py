n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sat = 0

for i in range(n):
  sat += b[a[i]-1]
  
  if i > 0 and a[i-1] == a[i]-1:
    sat += c[a[i]-2]

print(sat)