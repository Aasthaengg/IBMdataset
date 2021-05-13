def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    for i in range(1,n+1):
        u = 108*i//100
        if u == n:
            print(i)
            break
        elif u > n:
            print(':(')
            break


if __name__ == '__main__':
    main()