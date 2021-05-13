n = int(input())
c = list(input())

r = c.count('R')  
wr = c[:r].count('W')  

print(wr)