import sys
N,M,X = map(int,input().split())
array_gate = list(map(int,input().split()))
array_base = [0] * (N+1)

if not ( 1 <= N,M <= 100):
    sys.exit()
if not ( 1 <= X <= N -1 ):
    sys.exit()
if not ( 1 <= min(array_gate) <= max(array_gate) <= N - 1):
    sys.exit()

for I in range(len(array_base)):
    if I in array_gate:
        array_base[I] = 1

left = array_base[0:X]
right = array_base[X:-1]
if left.count(1) <= right.count(1):
    result = left.count(1)
else:
    result = right.count(1)

print(result)
