import itertools
x = int(input())
count = 0
coins = [ 100, 101 , 102 , 103 , 104 , 105]
for i in itertools.combinations_with_replacement(coins, x // 100):
  if sum(i) == x:
    count = 1
    break
print(count)