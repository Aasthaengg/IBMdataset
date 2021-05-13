N,K = (int(T) for T in input().split())
X = [int(T) for T in input().split()]
Cost = [0]*(N-K+1)
for T in range(0,N-K+1):
    Left  = X[T]
    Right = X[T+K-1]
    Cost[T] = min(abs(Left)+abs(Left-Right),abs(Right)+abs(Right-Left))
print(min(Cost))