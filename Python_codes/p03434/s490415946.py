n = int(input())
line = list(map(int, input().split()))
line.sort()
line.reverse()
A = 0
B = 0
for i in range(1,n+1):
  if i % 2 != 0:
    A += line[i-1]
  else:
    B += line[i-1]
print(A-B)