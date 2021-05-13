N = int(input())
S = input()

maxx = 0
x = 0
for c in S:
  if c == 'I':
    x += 1
    maxx = max(maxx, x)
  else:
    x -= 1
    
print(maxx)