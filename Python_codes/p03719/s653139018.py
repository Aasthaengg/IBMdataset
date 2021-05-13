import sys
import bisect
import heapq

sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline

def main():
    a,b,c = map(int,read().split())
    if a <= c and c <= b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
