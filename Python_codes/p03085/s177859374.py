import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

b = readline().rstrip().decode()
if b == 'A':
    print('T')
elif b == 'T':
    print('A')
elif b == 'G':
    print('C')
else:
    print('G')
