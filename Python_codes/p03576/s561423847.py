import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

def main():
    N,K = map(int,input().split())
    INF = float('inf')
    dot = []
    for _ in range(N):
        x,y = map(int,input().split())
        dot.append((x,y))
    
    dot.sort(key = itemgetter(0,1))
    ans = INF
    for xdown in range(N):
        for xup in range(N):
            if xup - xdown + 1 < K:
                continue
            else:
                use = dot[xdown:xup+1]
                a,b = use[-1][0],use[0][0]
                use.sort(key = itemgetter(1))
                l = len(use)
                for udown in range(l):
                    for uup in range(l):
                        if uup - udown + 1 == K:
                            two = use[udown:uup+1]
                            c,d = two[-1][1],two[0][1]
                            S = (a-b)*(c-d)
                            ans = min(ans,S)
                            
    print(ans)

if __name__ == "__main__":
    main()