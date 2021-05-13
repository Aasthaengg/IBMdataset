N = int(input())
AA = input().split()
BB = input().split()
CC = input().split()
total = 0
for i in range(len(AA)-1):
  if int(AA[i+1]) - int(AA[i]) == 1:
    
    total += int(CC[int(AA[i])-1])
    
for i in BB:
  total += int(i)
print(total)