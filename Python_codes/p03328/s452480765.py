a, b = map(int, input().split())

h_gnd = -b
for i in range(b - a):
  h_gnd += b - a - i
  
print(h_gnd)