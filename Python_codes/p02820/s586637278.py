import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
R, S, P = mapint()
T = list(input())

ans = 0
for i in range(N):
    t = T[i]
    if i<K:
        if t=='r':
            ans += P
        elif t=='s':
            ans += R
        else:
            ans += S
    else:
        if T[i-K]==T[i]:
            T[i] = '0'
            continue
        else:
            if t=='r':
                ans += P
            elif t=='s':
                ans += R
            else:
                ans += S  
print(ans)