a, b = map(int , input().split())

answer = -1
for i in range(1,10100):
  if i * 8 // 100 == a and i * 10 // 100 == b:
    answer = i
    break
    
print(answer)