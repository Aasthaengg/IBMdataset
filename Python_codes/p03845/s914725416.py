N = int(input())
T = [0] + list(map(int, input().split()))
M = int(input())
P = [0]
X = [0]
for _ in range(M):
    p, x = list(map(int, input().split()))
    P += [p]
    X += [x]
    
for i in range(1, M + 1):
    print(sum(T[1:]) - (T[P[i]] - X[i]))
