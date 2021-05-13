import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = LI()
h = LI()

ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)