N, X, T = map(int,input().split())
K = 0
while N>0:
    N -= X
    K += 1
print(T*K)