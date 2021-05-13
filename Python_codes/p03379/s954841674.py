import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
X = LI()
sort_X = sorted(X)
ans1,ans2 = sort_X[(N-1)//2],sort_X[N//2]
for x in X:
    if x>=ans2:
        print(ans1)
    else:
        print(ans2)
