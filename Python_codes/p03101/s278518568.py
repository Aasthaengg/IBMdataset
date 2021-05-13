import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    H, W = input_nums()
    h, w = input_nums()
    total = H*W
    print(total - (h*W + w*H - h*w))

if __name__ == '__main__':
    main()
