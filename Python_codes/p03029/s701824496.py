import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    a, p = input_nums()
    total = a * 3 + p
    print(total//2)

if __name__ == '__main__':
    main()
