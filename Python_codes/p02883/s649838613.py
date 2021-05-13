import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,K = map(int,S().split())
A = LI()
F = LI()
A = sorted(A)
F = sorted(F,reverse=True)

if sum(A) <= K:
    print(0)
    exit()

left = 0
right = 10**12
while left + 1 < right:
    mid = (left + right) // 2
    if sum(max(0,A[i]-mid//F[i]) for i in range(N)) <= K:
        right = mid
    else:
        left = mid

print(right)