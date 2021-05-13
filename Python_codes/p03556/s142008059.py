import sys,math
N = int(input())

if not ( 1 <= N <= 10 ** 9 ):
    sys.exit

root_N = math.floor(math.sqrt(N))
print(root_N ** 2)
