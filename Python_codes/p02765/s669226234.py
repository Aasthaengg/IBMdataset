import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,R = MI()
print(R if N >= 10 else R+100*(10-N))
