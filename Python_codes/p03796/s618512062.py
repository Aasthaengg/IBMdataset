import sys
import math
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(input())
    ans = math.factorial(N)%MOD
    print(ans)



if __name__ == '__main__':
    main()