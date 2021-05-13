import sys
def I(): return int(sys.stdin.readline().rstrip())

K = I()
print((K//2)**2 if K % 2 == 0 else (K**2-1)//4)
