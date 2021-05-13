import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

H,W = LI()
N = I()
a = LI()

ANS = []
for i in range(N):
    ANS += [i+1]*(a[i])

for i in range(H):
    if i % 2 == 0:
        print(*ANS[W*i:W*(i+1)])
    else:
        print(*reversed(ANS[W*i:W*(i+1)]))