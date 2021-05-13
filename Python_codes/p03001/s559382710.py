# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(W, H, x, y):
    print(W * H / 2, 1 if x * 2 == W and y * 2 == H else 0)

if __name__ == '__main__':
    input = sys.stdin.readline
    W, H, x, y = map(int, input().split())
    main(W, H, x, y)
