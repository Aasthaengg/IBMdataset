import sys
R = int(input())
G = int(input())
if not (0 <= R <= 4500 and 0 <= G <= 4500):
    sys.exit()

print ( G * 2 - R )