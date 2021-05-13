import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M,C = MI()
B = LI()
ans = 0
for i in range(N):
    A = LI()
    if C + sum(A[j]*B[j] for j in range(M)) > 0:
        ans += 1
print(ans)
