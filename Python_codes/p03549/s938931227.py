N,M = map(int,(input().split()))
T = 1900*M + 100*(N-M)
p = 2**M
print(T*p)