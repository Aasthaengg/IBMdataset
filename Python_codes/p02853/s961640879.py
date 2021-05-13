a, b = [int(x) for x in input().split()]
won = 0
if a in range(1, 4):
  won  += [0,300000,200000,100000][a]
if b in range(1, 4):
  won  += [0,300000,200000,100000][b]
if a == 1 and b == 1:won += 400000  
 
print(won)