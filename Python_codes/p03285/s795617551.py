N = int(input())
answer="No"

for i in range(26):
  for j in range(16):
    total = 4*i + 7*j
    
    if total==N:
      answer="Yes"

print(answer)