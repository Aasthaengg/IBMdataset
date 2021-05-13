import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,A,B = MI()
print((B-A)//2 if (B-A) % 2 == 0 else min((A+B-1)//2,N-(A+B-1)//2))
