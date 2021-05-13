import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 1
    for i in a:
        x *= i
    y = 0
    for i in a:
        y += x // i
    print(x / y)

if __name__ == '__main__':
    main()
