import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    x, a = input_nums()
    if x < a: print(0)
    else: print(10)

if __name__ == '__main__':
    main()