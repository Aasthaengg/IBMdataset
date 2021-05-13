import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,H = map(int,S().split())
ab = [LI() for i in range(N)]

A = [(ab[i][0],1) for i in range(N)]
B = [(ab[i][1],2) for i in range(N)]

from operator import itemgetter

C = sorted(A+B,key = itemgetter(0),reverse=True)

damage = 0  # 与ダメージ
ans = 0  # 攻撃回数
for i in range(2*N):
    if C[i][1] == 1:
        ans += (H-damage+C[i][0]-1)//C[i][0]
        break
    else:
        ans += 1
        damage += C[i][0]
        if damage >= H:
            break

print(ans)