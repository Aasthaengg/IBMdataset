import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
print(sum((i*(N//i)*(N//i+1)//2) for i in range(1,N+1)))
