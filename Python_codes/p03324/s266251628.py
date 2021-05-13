import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
D,N = LI()
sequence = []
for i in range(1,N+1):
    sequence.append(i*100**D)
ans = sequence[-1]

print(ans if N!=100 else ans +100**D)
