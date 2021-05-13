import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
V = LI()
C = LI()

ans = 0
for i in range(N):
    v,c = V[i],C[i]
    if v-c > 0:
        ans += v-c

print(ans)