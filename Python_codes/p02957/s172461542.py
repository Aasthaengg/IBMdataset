a,b = map(int, raw_input().split(' '))
if a > b:b,a = a,b
if (b - a) % 2 == 0: print a + (b-a)/2
else: print 'IMPOSSIBLE'