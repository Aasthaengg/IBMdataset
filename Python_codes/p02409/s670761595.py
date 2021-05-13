import sys
 
BUILDINGS = tuple(x for x in range(4))
FLOORS = tuple(x for x in range(3))
ROOMS = tuple(x for x in range(10))
 
occupant = [[[0 for r in ROOMS] for f in FLOORS] for b in BUILDINGS]
 
n = input() # 読み捨て
 
for line in sys.stdin:
    b, f, r, v = map(int, line.split())
    occupant[b - 1][f - 1][r - 1] += v
     
for b in BUILDINGS:
    if b:
        print('#' * 20)
    for f in FLOORS:
        print("", *occupant[b][f])