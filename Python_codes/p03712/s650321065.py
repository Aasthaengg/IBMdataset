from sys import stdin

h,w = [int(x) for x in stdin.readline().strip().split()]
output = "#" * (w+2)

for _ in range(h):
  output += "\n"
  output += "#" + stdin.readline().strip() + "#"
  
output += "\n" + "#" * (w+2)
print(output)