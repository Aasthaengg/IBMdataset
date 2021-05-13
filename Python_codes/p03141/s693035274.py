import sys
from operator import itemgetter
read = sys.stdin.read

N, *AB = map(int, read().split())
A = AB[::2]
B = AB[1::2]
ab = [a + b for a, b in zip(A, B)]
ab, A, B = zip(*sorted(zip(ab, A, B), key=itemgetter(0), reverse=True))
print(sum(A[::2]) - sum(B[1::2]))