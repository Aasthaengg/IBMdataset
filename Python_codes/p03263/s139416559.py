import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

H,W = map(int,S().split())
a = [LI() for _ in range(H)]

ANS = []
for i in range(H):
    for j in range(W):
        if j != W-1:
            if a[i][j] % 2 == 1:
                a[i][j+1] += 1
                ANS.append([i+1,j+1,i+1,j+2])
        else:
            if i != H-1:
                if a[i][j] % 2 == 1:
                    a[i+1][j] += 1
                    ANS.append([i+1,j+1,i+2,j+1])

print(len(ANS))

for i in range(len(ANS)):
    print(*ANS[i])