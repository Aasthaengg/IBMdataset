import sys
data = sys.stdin.readlines()
data = data[0].split()
N = int(data[0])
K = int(data[1])
if K == 1:
    print(0)
else:
    print(N-K)