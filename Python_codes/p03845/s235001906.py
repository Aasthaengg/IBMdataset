N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = []
X = []
SUM = sum(T)
for i in range(M):
    p,x = map(int, input().split())
    print(SUM-T[p-1]+x)