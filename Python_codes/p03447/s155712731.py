def main():
    import sys
    input = sys.stdin.readline
    X = int(input())
    A = int(input())
    B = int(input())
    print((X-A)%B)

if __name__ == '__main__':
    main()