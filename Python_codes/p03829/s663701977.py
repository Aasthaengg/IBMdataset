import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,A,B = MI()
X = LI()

# 左から考えていく

print(sum(min(B,A*(X[i+1]-X[i])) for i in range(N-1)))
