import sys
import math
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    n = math.ceil((-1 + math.sqrt(1+8*N))/2)
    jokyo = n*(n+1)//2 - N
    for i in range(1,n+1):
        if i == jokyo:
            continue
        else:
            print(i)
if __name__ == '__main__':
    main()
