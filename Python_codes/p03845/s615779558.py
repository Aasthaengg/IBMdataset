N = int(input())
T = list(map(int, input().split()))
M = int(input())
T_copy = T.copy()

for _ in range(M):
    T = T_copy.copy()
    P, X = map(int, input().split())
    T[P-1] = X
    print(sum(T))



