import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


L,R = MI()
if L//2019 != R//2019:  # 区間内に必ず2019の倍数がある
    print(0)
else:
    A = [i for i in range(L % 2019,(R % 2019)+ 1)]
    N = len(A)
    ans = 2019
    for i in range(N-1):
        for j in range(i+1,N):
            ans = min(ans,(A[i]*A[j]) % 2019)
    print(ans)
