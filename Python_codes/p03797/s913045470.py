import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    if 2*N >= M:
        print(M//2)
    else:
        rest = M-2*N
        print(N+rest//4)

if __name__ == "__main__":
    main()