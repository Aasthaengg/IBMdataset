import sys
def I(): return int(sys.stdin.readline().rstrip())


N,K = I(),I()
print(min(2**i+K*(N-i) for i in range(N+1)))
