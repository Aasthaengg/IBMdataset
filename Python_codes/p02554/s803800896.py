import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = int(readline())
    K = int(1e9) + 7
    ans = pow(10, N, K) - pow(9, N, K) - pow(9, N, K) + pow(8, N, K)
    print(ans%K)
if __name__ == '__main__':
    main()
