import sys

input = sys.stdin.readline

def main():
    n = int(input())
    A = list(map(int, input().split()))
    allB = exc = 1
    for i in A:
        allB *= 3
        if i%2 == 0:
            exc *= 2
    print(allB - exc)

if __name__ == '__main__':
    main()