import sys
def main():
    read = sys.stdin.read
    a, b, h = map(int, read().split())
    print((a + b) * h // 2)

if __name__ == '__main__':
    main()
