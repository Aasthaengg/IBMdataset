import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    r, D, x = input_nums()
    for i in range(10):
        x = r*x - D
        print(x)

if __name__ == '__main__':
    main()
