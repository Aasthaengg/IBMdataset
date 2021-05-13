import sys
N = int(input())
A = set()
for i in sys.stdin:
    A ^= {i}
print(len(A))