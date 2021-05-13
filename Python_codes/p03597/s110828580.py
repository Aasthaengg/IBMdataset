import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = int(input())

    print(max(0, N*N - A))

if __name__ == "__main__":
    main()