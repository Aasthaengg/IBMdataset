import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
AB = [LI() for _ in range(N)]
AB = sorted(AB, key=lambda x:x[1])
time = 0
for a,b in AB:
    time += a
    if time>b:
        print('No')
        break
else:
    print('Yes')
