import math
n = input()
money = 100
for i in xrange(n):
    money *= 1.05
    money = math.ceil(money)
print "%i"%(money*1000)