x = int(input())
yokin = 100
ans = 0
while yokin < (x):
  yokin = (yokin*100 +yokin)//100 
  ans += 1
print(ans)