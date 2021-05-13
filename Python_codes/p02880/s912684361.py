import sys
def I(): return int(sys.stdin.readline().rstrip())


A = [i*j for i in range(1,10) for j in range(1,10)]
print('Yes' if I() in A else 'No')
