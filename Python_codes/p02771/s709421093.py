from itertools import *

for a,b,c in permutations( map(int, input().split()), 3):
    if a==b and b != c:
        print("Yes")
        exit()

print("No")
