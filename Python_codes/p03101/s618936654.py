import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

input_n = lambda: int(readline())
input_nn = lambda: map(int, readline().split())
input_s = lambda: readline().rstrip().decode('utf-8')
input_ss = lambda: readline().rstrip().decode('utf-8').split()


def main():
    H, W = input_nn()
    h, w = input_nn()
    ans = H * W - (H * w + W * h - h * w)
    print(ans)


if __name__ == '__main__':
    main()
