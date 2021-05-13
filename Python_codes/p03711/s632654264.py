import sys
input = sys.stdin.readline


def main():
    A = {1, 3, 5, 7, 8, 10, 12}
    B = {4, 6, 9, 11}
    C = {2}
    xy = set(map(int, input().split()))
    if xy <= A or xy <= B or xy <= C:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()