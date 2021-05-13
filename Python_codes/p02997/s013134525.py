import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    full = (n-1)*(n-2)//2
    if k > full:
        print(-1)
    else:
        num = full-k
        print(num+n-1)
        for i in range(2, n+1):
            print(1, i)
        for i in range(2, n):
            for j in range(i+1, n+1):
                if num == 0:
                    exit()
                print(i, j)
                num -= 1


if __name__ == '__main__':
    main()