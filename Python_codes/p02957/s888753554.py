import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
geta = lambda fn: map(fn, readline().split())
gete = lambda fn: fn(readline())

# sys.setrecursionlimit(10**5)

def main():
    a, b = geta(int)
    s = a + b
    if s & 1 == 0:
        print(s//2)
    else:
        print("IMPOSSIBLE")
    
	
if __name__ == "__main__":
    main()