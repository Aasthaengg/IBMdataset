input_line = input().split()
x = int(input_line[0])
k = int(input_line[1])
d = int(input_line[2])

x = abs(x)
y = int(x/d)

if y < k:
  x -= y * d
  if (k-y) % 2 == 1:
    x -= d

else:
  x -= k*d
    
print(abs(x))
