import sys
a,b = map(int,input().split())

if not ( 1 <= a <= 9 and 1 <= b <= 9 ): sys.exit()
if not ( isinstance(a,int) and isinstance(b,int) ): sys.exit()

array_a = ''.join([ str(a) for z in range(b) ])
array_b = ''.join([ str(b) for z in range(a) ])
array = [array_a,array_b]
array.sort()

print(array[0])