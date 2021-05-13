def main():
    import sys
    readline = sys.stdin.buffer.readline

    a, b = map(int, readline().split())
    print(a*b if a < 10 and b < 10 else -1)

if __name__ == '__main__':
    main()