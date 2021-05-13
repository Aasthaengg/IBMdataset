a, b, k = map(int, input().split())

answer = []
for i in range(0,k):
  if a+i <= b:
    answer.append(a+i)
  else:
    break
  
for i in range(0,k):
  if b-i >= a:
    answer.append(b-i)
  else:
    break  
    
answer = list(set(answer))  
answer.sort()

for a in answer :
  print(a)