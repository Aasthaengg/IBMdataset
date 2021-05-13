import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
p = [0] + LI()

# 左から貪欲に

ans = 0
for i in range(1,N+1):
    if p[i] == i:
        if i < N:
            ans += 1
            p[i],p[i+1] = p[i+1],p[i]
        else:
            ans += 1

print(ans)