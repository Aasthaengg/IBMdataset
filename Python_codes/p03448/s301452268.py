five = int(input()) + 1
hand = int(input()) + 1
fives = int(input()) + 1
ans = int(input()) 
tmp = 0
 
for i in range(five):
  for j in range(hand):
    for k in range(fives):
      ask = 500 * i + 100 * j + 50 * k
      if ans == ask:
        tmp = tmp + 1

print(tmp)