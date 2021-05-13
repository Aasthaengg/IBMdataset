import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M,C = MI()
B = LI()
ans = 0
for i in range(N):
    A = LI()
    a = C
    for j in range(M):
        a += A[j]*B[j]
    if a > 0:
        ans += 1
print(ans)
