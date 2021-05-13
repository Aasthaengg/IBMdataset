import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    A, B, C = map(int, readline().split())
    if A%2==0 or B%2==0 or C%2==0:
        ans = 0
    else:
        ans = min(A*B, B*C, C*A)
    print(ans)



if __name__ == '__main__':
    main()