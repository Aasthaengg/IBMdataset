import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし


N = I()
X = LI2()
X.reverse()

if N == 0:
    print(1)
    exit()

A = [0]*(2*10**5+1)  # Ai = f(i)
for i in range(1,2*10**5+1):
    k = 0
    for j in range(18):
        if (i >> j) & 1:
            k += 1
    A[i] = A[i % k] + 1


r = sum(X)  # Xの各桁の和

if r >= 2:
    B = [1] + [0]*(N-1)  # Bi = 2**i mod (r-1)
    C = [1] + [0]*(N-1)  # Ci = 2**i mod (r+1)
    b,c = X[0],X[0]  # b,c = X mod (r-1),X mod (r+1)
    for i in range(1,N):
        B[i] = (B[i-1]*2) % (r-1)
        C[i] = (C[i-1]*2) % (r+1)
        if X[i] == 1:
            b += B[i]
            b %= r-1
            c += C[i]
            c %= r+1

    for i in range(N-1,-1,-1):
        if X[i] == 0:
            print(1+A[(c+C[i]) % (r+1)])
        else:
            print(1+A[(b-B[i]) % (r-1)])

else:
    C = [1] + [0]*(N-1)  # Ci = 2**i mod (r+1)
    c = X[0]  # c = X mod (r+1)
    for i in range(1,N):
        C[i] = (C[i-1]*2) % (r+1)
        if X[i] == 1:
            c += C[i]
            c %= r+1

    for i in range(N-1,-1,-1):
        if X[i] == 0:
            print(1+A[(c+C[i]) % (r+1)])
        else:
            print(0)
