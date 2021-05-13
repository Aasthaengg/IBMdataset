import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        l, r, d = map(int, input().split())
        E[l-1].append((r - 1, d))
        E[r-1].append((l - 1, -d))
    Pos = [10 ** 20] * N
    q = deque()
    flag = True
    for i in range(N):
        if Pos[i] == 10 ** 20:
            q.append((i, 0))
            minX, maxX = 0, 0
            while q:
                x, p = q.popleft()
                if Pos[x] == 10 ** 20:
                    minX = min(minX, p)
                    maxX = max(maxX, p)
                    Pos[x] = p
                    for ne, d in E[x]: q.append((ne, p + d))
                elif Pos[x] == p: continue
                else:
                    flag = False
                    break
            else:
                if maxX - minX <= 10 ** 9: continue
                else: flag = False
            if not flag:
                print("No")
                break
    else: print("Yes")
    #print(Pos)
            
    return 0

if __name__ == "__main__":
    solve()