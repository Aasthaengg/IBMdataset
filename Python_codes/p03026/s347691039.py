import sys
input = sys.stdin.readline
from collections import deque

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        l,r = map(int,input().split())
        edge[l-1].append(r-1)
        edge[r-1].append(l-1)

    a = list(map(int,input().split()))
    a.sort(reverse = True)
    put = [-1 for _ in range(N)]
    put[0] = a[0]
    q = deque([0])
    i = 1
    while q:
        now = q.popleft()
        for fol in edge[now]:
            if put[fol] != -1:
                continue
            else:
                put[fol] = a[i]
                i += 1
                q.append(fol)
    
    print(sum(a)-a[0])
    print(*put)
    
if __name__ == "__main__":
    main()

