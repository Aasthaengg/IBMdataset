import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
T,A = MI()
H = [abs(T-i*0.006-A) for i in LI()]
m = min(H)
print(H.index(m)+1)

