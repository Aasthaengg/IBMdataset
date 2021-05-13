import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
inpl = lambda: list(map(int,input().split()))
N = int(input())
CAB = []
for _ in range(N):
    A, B = inpl()
    CAB.append((A+B,A,B))
CAB.sort(reverse=True)
ans = sum(CAB[i][1] for i in range(0,N,2)) - sum(CAB[i][2] for i in range(1,N,2))
print(ans)