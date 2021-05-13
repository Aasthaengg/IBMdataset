import sys
def S(): return sys.stdin.readline().rstrip()

b = S()
if b == 'A':
    print('T')
elif b == 'T':
    print('A')
elif b == 'C':
    print('G')
else:
    print('C')