import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N = I()
D = [0]*N
for i in range(N):
    a,b = MI()
    if a == b:
        D[i] = 1

for i in range(N-2):
    if D[i] == D[i+1] == D[i+2] == 1:
        print('Yes')
        break
else:
    print('No')
