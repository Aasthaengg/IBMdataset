import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    a, b, c = input_nums()
    if b//a > c: print(c)
    else: print(b//a)

if __name__ == '__main__':
    main()
