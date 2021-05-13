import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    total = 3**N
    odd = 1
    for i in range(N):
        if A[i]%2==0:
            odd *= 2
    print(total-odd)

if __name__ == '__main__':
    main()