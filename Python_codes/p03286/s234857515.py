import sys

N = int(input())
if not N:
    print(0)
    sys.exit()
    
S = ''

while N:
    r = N%2
    N = N//(-2)+r
    S += str(r)

print(S[::-1])