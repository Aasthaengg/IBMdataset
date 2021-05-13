import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = map(int, input().split())
from collections import defaultdict
ns = defaultdict(set)
for i in range(m):
    u,v,c = map(int,input().split())
    u -= 1
    v -= 1
    ns[u].add((c,v))
    
score = [None]*n
score[0] = 0
prev = score
for i in range(n+3):
    update = False
    for u in range(n):
        if prev[u] is not None:
            for c,v in ns[u]:
                if score[v] is None or score[v]<prev[u]+c:
                    score[v] = prev[u]+c
                    update = True
    if not update:
        print(score[-1])
        break
    prev = score
else:
    reach = [False]*n
    for i in range(n+1):
        for u in range(n):
            if prev[u] is not None:
                for c,v in ns[u]:
                    if score[v] is None or score[v]<prev[u]+c:
                        score[v] = prev[u]+c
                        reach[v] = True
    if reach[-1]:
        print("inf")
    else:
        print(score[-1])