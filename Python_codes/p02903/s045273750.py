import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


H,W,A,B = MI()
for _ in range(B):
    print(''.join(['0']*A+['1']*(W-A)))
for _ in range(H-B):
    print(''.join(['1']*A+['0']*(W-A)))
