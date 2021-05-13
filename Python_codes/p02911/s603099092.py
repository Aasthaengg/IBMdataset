import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K,Q = MI()

X = [0]*(N+1)  # 各参加者の正解数
for _ in range(Q):
    a = I()
    X[a] += 1

for i in range(1,N+1):
    x = X[i]
    print('Yes' if K-(Q-x) > 0 else 'No')
