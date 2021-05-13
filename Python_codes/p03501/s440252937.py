import sys
import bisect
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline

def main():
    n,a,b = map(int,read().split())
    print(min(a*n,b))
    
if __name__ == '__main__':
    main()
