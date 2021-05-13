import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()


X,Y,Z,K = map(int,S().split())
A = LI()
B = LI()
C = LI()

A = [0] + sorted(A,reverse = True)
B = [0] + sorted(B,reverse = True)
C = [0] + sorted(C,reverse = True)

ANS = []

# i+j+k <= K の範囲だけ考えればよい
for i in range(1,X+1):
    for j in range(1,min(K//i+1,Y)+1):
        for k in range(1,min(K//(i*j)+1,Z)+1):
            ANS.append(A[i]+B[j]+C[k])

ANS = sorted(ANS,reverse=True)

for i in range(K):
    print(ANS[i])