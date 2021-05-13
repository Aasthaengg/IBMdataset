import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
V = LI()

ans = 0
for i in range(K+1):  # 操作回数
    for j in range(N+1):  # 左から取る個数
        for k in range(N+1):  # 右から取る個数
            if j + k > min(N,i):
                break
            l = i-j-k  # 戻す個数
            if l > j+k:
                continue
            A = [V[m] for m in range(j)] + [V[N-1-m] for m in range(k)]
            A.sort(reverse=True)
            ans = max(ans,sum(A[m] for m in range(j+k-l)))
print(ans)
