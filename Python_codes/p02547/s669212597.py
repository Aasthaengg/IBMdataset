n = int(input())

lists = []

count = 0

while n:
  
  doublets = tuple(map(int, input().split()))
  lists.append(doublets)

  n -= 1

for x,y in lists:
  if x == y:
    count += 1
    continue
  elif count == 3:
   	break
  else:
   	count = 0
if (count >= 3):
    print('Yes')
else:
    print('No')