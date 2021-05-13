import sys
def I(): return int(sys.stdin.readline().rstrip())
a,b,h = [I() for _ in range(3)]
print((a+b)*h//2)
