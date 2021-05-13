import sys
import statistics                                                                                                                       
readInt = lambda f=sys.stdin: [int(i) for i in f.readline().split()];
n = readInt()[0]
A = readInt()
C = [a - i for i, a in enumerate(A)]
b = int(statistics.median(C))
ans = sum([abs(c - b) for c in C])

print(ans)