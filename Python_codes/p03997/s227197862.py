import sys
def I(): return int(sys.stdin.readline().rstrip())

a,b,h = I(),I(),I()
print((a+b)*h//2)