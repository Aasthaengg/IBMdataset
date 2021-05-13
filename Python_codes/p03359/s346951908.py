import sys
a,b = map(int,input().split())

if not ( 1 <= a <= 12 and 1 <= b <= 31 ):
    sys.exit()

print(a) if a <= b else print(a-1)