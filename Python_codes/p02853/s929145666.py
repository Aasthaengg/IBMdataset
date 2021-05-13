c1, c2 = map(int, input().split())

prizes = [300000, 200000, 100000]
total_prize = 0
if(c1 <= 3):
  total_prize += prizes[c1-1]
if(c2 <= 3):
  total_prize += prizes[c2-1]
if(c1==1 and c2==1):
  total_prize += 400000
print(total_prize)