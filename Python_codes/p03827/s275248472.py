n = int(input())
s = input()

x = 0
max = 0

for i in range(n):
  if s[i] == 'I':
    x += 1
    if max < x:
      max =x 
  else:
    x -= 1
    
print(max)