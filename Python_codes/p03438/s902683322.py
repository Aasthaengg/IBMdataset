def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    sm = 0
    for x, y in zip(a,b):
        tmp = y-x
        sm += tmp
        if tmp > 0:
            tmp //= 2
        s += tmp
    if s >= 0 and sm >= 0:
        print('Yes')
    else:
        print('No')

    
if __name__ == '__main__':
    main()