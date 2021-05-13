import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    a, b = input_nums()
    if b*2 >= a:
        print(0)
    else:
        print(a-b*2)

if __name__ == '__main__':
    main()