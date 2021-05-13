import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
K = I()
x = LI()

print(2*sum(min(x[i],K-x[i]) for i in range(N)))