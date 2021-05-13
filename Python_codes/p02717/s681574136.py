import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    X, Y, Z = input_nums()
    print(Z, X, Y)

if __name__ == '__main__':
    main()