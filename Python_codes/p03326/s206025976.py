import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M = LI()
xyz = [LI() for i in range(N)]

# x+y+z,x+y-z,x-y+z,x-y-z,-x+y+z,-x+y-z,-x-y+z,-x-y-z たちの和の大きい方からM個を足す

ANS = []
for i in range(2**3):
    A = []
    for j in range(3):
        if (i >> j) & 1:
            A.append(1)
        else:
            A.append(-1)
    B = []
    for j in range(N):
        B.append(sum(xyz[j][k]*A[k] for k in range(3)))
    B.sort(reverse=True)
    ANS.append(sum(B[j] for j in range(M)))

print(max(ANS))