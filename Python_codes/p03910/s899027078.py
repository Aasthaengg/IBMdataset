n = int(input())

aa =[]
i = 0
score = 0

while score < n:
  i += 1
  score += i
  aa.append(i)
  
if score == n:
  for k in range(len(aa)):
    print(aa[k])
    
else:
  aa.remove(score - n)
  for k in range(len(aa)):
    print(aa[k])