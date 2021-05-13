import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Hs = list(mapint())+[0]

ans = 0
while 1:
    cnt = 0
    start = False
    for i in range(N+1):
        if Hs[i]!=0:
            start = True
            Hs[i] -= 1
        else:
            if start:
                cnt += 1
            start = False
    ans += cnt
    if sum(Hs)==0:
        break
print(ans)