import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


K,T = MI()
A = LI()
print(max(0,2*max(A)-K-1))
