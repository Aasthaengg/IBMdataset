D, N = map(int, input().split())
print(N * 10**(2*D) if N != 100 else (N+1) * 10**(2*D))
