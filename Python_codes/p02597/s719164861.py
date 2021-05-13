n = int(input())
c = input()
 
r = c.count('R')
ans = c[0:r].count('W')
 
print(ans)