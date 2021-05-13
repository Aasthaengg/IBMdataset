import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

set_ = set(S)
for c in [chr(i) for i in range(97, 97+26)]:
    if c not in set_:
        print(c)
        quit()
print('None')