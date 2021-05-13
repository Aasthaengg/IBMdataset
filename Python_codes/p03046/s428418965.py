import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

M,K = MI()

if K >= 2**M or (M == 1 and K == 1):
    print(-1)
elif M == 1 and K == 0:
    print(*[0,0,1,1])
else:
    A = [i for i in range(2**M) if i != K]
    ANS = A + [K] + list(reversed(A)) + [K]
    print(*ANS)
