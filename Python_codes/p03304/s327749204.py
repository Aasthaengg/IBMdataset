N,M,D=map(int, input().split())
a=(N-D)*2 if D else N
print((a/N**2)*(M-1))