import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
print(max((N-1)//I() for _ in range(5)) + 5)
