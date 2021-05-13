import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))


if __name__ == "__main__":
    main()