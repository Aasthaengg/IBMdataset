from collections import deque
import sys
input = sys.stdin.readline  #文字列入力では注意！

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
for _ in range(M):
    L,R,D = map(int,input().split())
    L -= 1; R -= 1
    Graph[L].append((R,D))
    Graph[R].append((L,-D))

num = dict()
for i in range(N):
    if i not in num:
        num[i] = 0
        Q = deque(Graph[i])
        x = 0
        while Q:
            now,d = Q.popleft()
            if now in num:
                if num[now] != d:
                    print("No")
                    exit()
            else:
                num[now] = d
                for node,Di in Graph[now]:
                    Q.append((node,d+Di))
print("Yes")
