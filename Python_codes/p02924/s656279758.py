import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())

    def sum_up_to_n(n):
        return n * (n + 1) // 2

    print(sum_up_to_n(N - 1))
    

if __name__ == '__main__':
    main()

