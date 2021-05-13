import sys
input = sys.stdin.readline
def main():
    N, D = map(int, input().split())
    R = 2*D +1
    print((N+R-1)//R)

if __name__ == '__main__':
    main()