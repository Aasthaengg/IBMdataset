from collections import deque
import sys
N, M = map(int, input().split())
K = [[] for _ in range(N)]
for i in range(M):
    L, R, D = map(int, input().split())
    K[L-1].append([R-1, D])
    K[R-1].append([L-1, -D])
used = [0]*(N+1)
Num = [10**12]*(N+1)
for i in range(N):
    large = 0
    small = 0
    if used[i] == 0:
        used[i] = 1
        Num[i] = 0
        P = deque([i])
        while(True):
            if len(P) == 0:
                break
            a = P.popleft()
            for s, m in K[a]:
                if Num[s] == 10**12:
                    Num[s] = Num[a] + m
                else:
                    if Num[s] != Num[a]+m:
                        print("No")
                        sys.exit()
                large = max(large, Num[s])
                small = min(small, Num[s])
                if used[s] == 0:
                    used[s] = 1
                    P.append(s)
        if large - small > 10**9:
            print("No")
            sys.exit()
print("Yes")