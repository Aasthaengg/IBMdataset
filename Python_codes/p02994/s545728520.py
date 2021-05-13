N, L = map(int, input().split())
m, p = 100000, 0
A = [abs(L+i-1) for i in range(1, N+1)]
print(sum(L+i-1 for i in range(1, N+1)) -(L+A.index(min(A))))