import sys
a,b = map(int,input().split())

if not (1 <= a <= 10000 and 1 <= b <= 10000):
    sys.exit()

print('Odd') if (a * b) % 2 == 1 else print('Even')
