import sys
A,B = map(int,input().split())

if not (1 <= A <= 16 and 1 <= B <= 16 and (A + B <= 16)) :
    sys.exit()

print('Yay!') if A <= 8 and B <= 8 else print(':(')