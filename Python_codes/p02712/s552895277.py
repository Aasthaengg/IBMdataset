import sys

N = int(input())
array = [ a for a in range(1,N+1) if a % 3 != 0 ]
array = [ b for b in array if b % 5 != 0 ]

if not ( 1 <= N <= 10**6 ): sys.exit()
print(sum(array))
