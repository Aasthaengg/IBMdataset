N = int(input())
c = input()
Rn = c.count("R")
c2 = c[:Rn]
res = c2.count("W")
print(res)