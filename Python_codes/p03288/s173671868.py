import sys
R = int(input())

if not (0 <= R <= 4208):
    sys.exit()

print('ABC') if R < 1200 else print('ARC') if R < 2800 else print('AGC')