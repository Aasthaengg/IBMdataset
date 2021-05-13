import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    min_id = 0
    max_id = 10**5
    for _ in range(M):
        L, R = map(int, input().split())
        if min_id < L:
            min_id = L
        if max_id > R:
            max_id = R
    if min_id > max_id:
        print(0)
    else:
        print(max_id - min_id + 1)


if __name__ == '__main__':
    main()
