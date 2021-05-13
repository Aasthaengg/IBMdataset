def main():
    import sys
    readline = sys.stdin.buffer.readline

    a, b = map(int, readline().split())
    print(max(0, a-b-b))

if __name__ == '__main__':
    main()