import sys
import math
 
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
 
def main():
    s = map(int,input().split())
    print(len(set(s)))
    
if __name__ == '__main__':
    main()