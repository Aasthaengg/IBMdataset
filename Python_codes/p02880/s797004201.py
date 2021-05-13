def main():
    import sys
    readline = sys.stdin.buffer.readline

    n = int(readline())
    for i in range(1, 10):
        for j in range(i, 10):
            if i*j == n:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()