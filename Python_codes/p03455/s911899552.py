import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    m = a * b
    if m % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    main()