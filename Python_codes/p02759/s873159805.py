n = int(input())
min = 0

if n%2 == 0:
  min = n/2
else:
  min = n//2 + 1

print(int(min))