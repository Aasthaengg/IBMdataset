import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


K = I()
A = LI()
A.reverse()

m,M = 2,2  # 最小値、最大値
for i in range(K):
    a = A[i]
    if (m+(a-1))//a > M//a:
        print(-1)
        exit()
    else:
        m = a*((m+(a-1))//a)
        M = a*(M//a)+(a-1)

print(m,M)
