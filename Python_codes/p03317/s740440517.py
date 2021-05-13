import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
A = LI()

print((N+K-3)//(K-1))
