import sys
a = sys.stdin.readline()
A = int(a)
P = 1
I = 1 
W = 10 ** 9 + 7
while I <= A:
    P *= I
    I += 1
    P %= W
print(P)