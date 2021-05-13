import sys
N,K = map(int,input().split())
if not (1 <= N <= 100 and 1 <= K <= 100):
    sys.exit()

print(0) if N % K == 0 else print(1)