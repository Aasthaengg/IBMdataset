def main():
    import sys
    readline = sys.stdin.buffer.readline

    n = int(readline())
    a = int(n**(1/2)//1)
    for i in range(a, 0, -1):
        b, m = divmod(n, i)
        if m == 0:
            print(i+b-2)
            exit()

if __name__ == '__main__':
    main()