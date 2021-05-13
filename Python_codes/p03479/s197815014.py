x,y = input().split()
X = int(x)
Y = int(y)

A = X
count = 0
while Y >= A:
  A = A*2
  count += 1

print(count)