n, m = input().split()
N = int(n)
M = int(m)
print(int(((N+M)*(N+M-1))/2) - N * M)