import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    k, x = map(int, input().split())
    black = [i for i in range(x-(k-1), x+k)]
    print(*black)

if __name__ == '__main__':
    main()