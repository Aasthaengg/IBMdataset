import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    print(sum(A[1:2*N:2]))


if __name__ == '__main__':
    main()
