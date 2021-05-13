import sys
X = int(input())
A = int(input())
B = int(input())

if not ( 1 <= A <= 1000 and 1 <= B <= 1000):
    sys.exit()
if not (A + B <= X <= 10000):
    sys.exit()

print((X - A) % B )
