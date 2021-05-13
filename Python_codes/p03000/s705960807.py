import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,X = MI()
L = LI()

a = 0
ans = 1
for i in range(N):
    a += L[i]
    if a <= X:
        ans += 1

print(ans)
