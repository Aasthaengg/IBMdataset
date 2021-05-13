X = int(input())
t = 1
for t in range(1,X+1):
  total = t*(t+1)/2
  if total>=X:
    break
print(t)