import sys
N,L = map(int,input().split())

if not ( 2 <= N <= 200 and -100 <= L <= 100 ): sys.exit()

array = [ L+x for x in range(N)]
before = 100
for I in array:
    if abs(I) <= before: before = abs(I);position = array.index(I)
print(sum(array) - array[position])