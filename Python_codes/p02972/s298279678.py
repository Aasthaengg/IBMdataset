import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = [0] + list(map(int,read().split()))

for n in range(N//2,0,-1):
    A[n] = sum(A[n::n])&1

I = [i for i, x in enumerate(A) if x]

print(len(I))
if len(I) > 0:
    print(' '.join(map(str,I)))