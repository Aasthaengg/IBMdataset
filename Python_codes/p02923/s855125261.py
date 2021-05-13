n = int(input())
hn = [int(num) for num in input().split()]

answer = 0
count = 0
for index in range(1,len(hn)):
  if hn[index-1] >= hn[index]:
    count += 1
  else :
    if answer < count:
      answer = count
    count = 0

if answer < count:
  answer = count
    
print(answer)