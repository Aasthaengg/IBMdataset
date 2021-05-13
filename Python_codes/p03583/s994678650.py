import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    for n in range(1,3501):
        for h in range(1,3501):
            x = 4*n*h-N*n-N*h
            if x<=0:
                continue
            else:
                if (N*h*n)%x==0:
                    print(n, h, (N*h*n)//x)
                    exit()


if __name__ == '__main__':
    main()