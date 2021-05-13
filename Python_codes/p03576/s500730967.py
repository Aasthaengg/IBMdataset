import copy
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, K = LI()
x = [0]*N; y = [0]*N
for i in range(N):
    x[i], y[i] = LI()

X = copy.deepcopy(x); Y = copy.deepcopy(y)
X.sort(); Y.sort()

Xcandi = [0]*2; Ycandi = [0]*2
ylower = 0; yupper = N-1; ycur = (ylower+yupper)//2
ansC = []
for i in range(N-1):
    Xcandi[0] = X[i]
    for j in range(i+1,N):
        Xcandi[1] = X[j]
        for k in range(N-1):
            ylower = k+1; yupper = N - 1; ycur = (ylower + yupper) // 2
            Ycandi[0] = Y[k]
            while(True):
                cur = int(0)
                Ycandi[1] = Y[ycur]
                for l in range(N):
                    if Xcandi[0] <= x[l] <= Xcandi[1] and Ycandi[0] <= y[l] <= Ycandi[1]:
                        cur += 1
                if yupper - ylower >= 2:
                    if cur < K:
                        ylower = ycur
                        ycur = (ycur + yupper) // 2
                    else:
                        yupper = ycur
                        ycur = (ycur + ylower) // 2
                else:
                    cur = int(0)
                    Ycandi[1] = Y[yupper]
                    for l in range(N):
                        if Xcandi[0] <= x[l] <= Xcandi[1] and Ycandi[0] <= y[l] <= Ycandi[1]:
                            cur += 1
                    if cur < K:
                        break
                    else:
                        cur = int(0)
                        Ycandi[1] = Y[ylower]
                        for l in range(N):
                            if Xcandi[0] <= x[l] <= Xcandi[1] and Ycandi[0] <= y[l] <= Ycandi[1]:
                                cur += 1
                        if cur < K:
                            Ycandi[1] = Y[ylower+1]
                    cur = (Xcandi[1] - Xcandi[0])*(Ycandi[1] - Ycandi[0])
                    ansC.append(cur)
#                    print(Xcandi,Ycandi)
                    break


#print(ansC)
print(min(ansC))
