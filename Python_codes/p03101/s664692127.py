import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    print(H * W - (h * W + w * H - h * w))

if __name__ == '__main__':
    main()
