def main():
    import sys
    def input(): return sys.stdin.readline()[:-1]
    pl = lambda x: print(*x, sep='\n')

    A, B, K = map(int, input().split())

    for val in range(A, B+1):
        if val<=A+K-1 or B-K+1<=val:
            print(val)

if __name__ == '__main__':
    main()