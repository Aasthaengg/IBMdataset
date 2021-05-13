import sys
input = sys.stdin.buffer.readline
import heapq
from collections import defaultdict
from operator import itemgetter

def main():
    N,K = map(int,input().split())
    sushi = []
    for _ in range(N):
        t,d = map(int,input().split())
        sushi.append((-d,t))
    sushi.sort(key=itemgetter(0))
    use,only,unuse = [],[],sushi[K:]
    neta = defaultdict(int)
    x = 0
    for i in range(K):
        d,t = sushi[i]
        if neta[t] == 0:
            only.append((-d,t))
        else:
            use.append((-d,t))
        neta[t] += 1
        x -= d
    
    l = len(neta)
    heapq.heapify(use)
    heapq.heapify(only)
    heapq.heapify(unuse)
    
    ans = x + l**2
    while (len(use) != 0 and len(unuse) != 0 and l < K):
        cd,ct = heapq.heappop(unuse)
        cd *= -1
        if neta[ct] != 0:
            continue
        heapq.heappush(only,(cd,ct))
        rd,rt = heapq.heappop(use)
        x += cd-rd
        l += 1
        neta[ct] += 1
        neta[rt] -= 1
        ans = max(ans,x+l**2)
        
    print(ans)

if __name__ == "__main__":
    main()