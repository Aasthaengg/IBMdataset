s = input()
score = 0 
g = 0 
for i in s:
  if g == 0:
    g += 1
    if i == "p":
      score -= 1
  elif g == 1:
    g -= 1
    if i == 'g':
      score += 1
print(score)