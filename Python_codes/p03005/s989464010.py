import sys
args = sys.stdin.readlines()
tmp = [int(x) for x in args[0].split(' ')]
N, K = tmp[0], tmp[1]

if K == 1:
    print(0)
    exit()
print(N-K)