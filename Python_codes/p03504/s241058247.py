import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,C = list(map(int, input().split()))
stc = [tuple(map(int, input().split())) for _ in range(n)]
T = max(item[1] for item in stc)
l = [[False]*(T+1) for _ in range(C)]
for s,t,c in stc:
    for i in range(s-1,t):
        l[c-1][i] = True
ans = max(sum(l[c][i] for c in range(C)) for i in range(T+1))
print(ans)