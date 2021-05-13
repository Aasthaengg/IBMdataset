import sys
N = int(input())
test = lambda x: [ x[0],int(x[1]) ]
array = [ [test(input().split()),int(x+1)] for x in range(N) ]

if not ( 1 <= N <= 100 ): sys.exit()
for I in array:
    if not ( 1 <= len(I[0][0]) <= 10 ): sys.exit()
    if not I[0][0].islower(): sys.exit()
    if not ( 0 <= I[0][1] <= 100 ): sys.exit()
    if not isinstance(I[0][1],int): sys.exit()

array.sort(key=lambda x: x[0][1], reverse=True)
array.sort(key=lambda x: x[0][0])

for I in array:
    print(I[1])