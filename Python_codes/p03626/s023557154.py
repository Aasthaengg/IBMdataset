import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N = I()
cur = 0
ans = []; S = [[] for _ in range(2)]
for i in range(2):
    S[i] = str(input())
#print(S[0][0])
C = []
i = int(0)
while i<=N-1:
    if S[0][i]==S[1][i]:
        C.append(0)
        i +=1
    else:
        C.append(1)
        i +=2
#print(C)
cur = int(1)
for i in range(len(C)):
    if i==0:
        if C[i]==0:
            cur *= 3
        else:
            cur *= 6
    else:
        if not (C[i-1]==1 and C[i]==0):
            if (C[i-1]==1 and C[i]==1):
                cur *=3
            else:
                cur *= 2

ans = cur%mod
print(ans)