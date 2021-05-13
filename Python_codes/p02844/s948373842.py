import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

N = I()
S = LI2()
ans = 0
for i in range(1000):
    x = str(i).zfill(3)
    X = [int(x[0]),int(x[1]),int(x[2])]
    j = 0
    k = 0
    while j < N:
        if S[j] == X[k]:
            if k == 2:
                ans += 1
                break
            else:
                k += 1
        j += 1

print(ans)
