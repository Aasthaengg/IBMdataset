import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
Bs = list(mapint())

if sum(As)<sum(Bs):
    print(-1)
else:
    minus = 0
    cnt = 0
    lis = []
    for a, b in zip(As, Bs):
        if a<b:
            minus += (b-a)
            cnt += 1
        else:
            lis.append(a-b)
    lis.sort(reverse=True)
    if minus==0:
        print(0)
    else:
        for l in lis:
            minus -= l
            cnt += 1
            if minus<=0:
                break
        print(cnt)