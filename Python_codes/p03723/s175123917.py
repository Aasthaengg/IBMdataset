import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    A, B, C = [int(x) for x in input().split()]

    cnt = 0
    while True:
        if cnt > 10 ** 5:
            print(-1)
            return

        if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
            print(cnt)
            return

        A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
        cnt += 1
       

if __name__ == '__main__':
    main()
