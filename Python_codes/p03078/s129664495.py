import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


X,Y,Z,K = MI()
A,B,C = LI(),LI(),LI()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

ANS = []
for i in range(X):
    if i >= K:
        break
    a = A[i]
    for j in range(Y):
        if i*j >= K:
            break
        b = B[j]
        for k in range(Z):
            if i*j*k >= K:
                break
            c = C[k]
            ANS.append(a+b+c)

ANS.sort(reverse=True)
print(*ANS[:K],sep='\n')
