N, M, X = map(int, input().split())
A = list(map(int, input().split()))
B = len([a for a in A if a<X])
print(B if B<M//2 else M-B)