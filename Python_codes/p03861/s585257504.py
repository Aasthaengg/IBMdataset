from decimal import *
import math
#exp = Decimal(10**23)
#rint((Decimal(11)*exp)/Decimal(10))

## coding: UTF-8
s = input().split()
t = [int(p) for p in s]
#print(t)

a = t[0]
b = t[1]
x = t[2]
if(a != 0):
    print(b // x - (a-1) // x)
else:
    print(b // x + 1)
'''
n = math.floor(Decimal(b-a+1) / Decimal(x))

p = (b-a+1) % x
if(p > 0):
    l = a % x
    if(l <= p-1):
        n += 1
print(n)
'''

'''
start = a
goal = b
while True:
    if(start % x == 0):
        break
    else:
        start += 1
#print(start)
while True:
    if(goal % x == 0):
        break
    else:
        goal -= 1
#start = Decimal(3)
#goal = Decimal(999999999999999999)

#print(Decimal(goal))
print(Decimal(Decimal(Decimal(goal) - Decimal(start)) / Decimal(x)) + Decimal(1)  ) 
#answer = ((goal - start) / x ) + 1
#print('{}'.format(int(answer)))
'''
'''
#AC code
def count_even(t, x):
    return int( Decimal(t)/ Decimal(x) )

if( a == 0):
    answer = count_even(b, x) + 1
else:
    answer = count_even(b, x) - count_even(a-1, x)
print(answer)
'''