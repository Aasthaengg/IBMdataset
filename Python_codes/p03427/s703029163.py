import sys
import time
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = input()
    L = len(N)
    if L == 1:
        ans = int(N)
    elif set(N[1:]) == {'9'}:
        ans = int(N[0]) + 9*(L-1)
    else:
        ans = (int(N[0])-1) + 9*(L-1)
    print(ans)
if __name__ == '__main__':
    main()