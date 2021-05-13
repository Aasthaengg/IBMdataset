import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


K,S = MI()

print(sum(0 <= S-i-j <= K for i in range(K+1) for j in range(K+1)))
