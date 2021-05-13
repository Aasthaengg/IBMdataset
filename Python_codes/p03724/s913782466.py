import sys
from collections import Counter
read = sys.stdin.read

N, M, *ab = map(int, read().split())
answer = [1 for i in Counter(ab).values() if i % 2 == 1]

if not answer:
    print('YES')
else:
    print('NO')