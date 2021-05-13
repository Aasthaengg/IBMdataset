import math


def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    index_one = A.index(1)
    min_cnt = N
    for left_index in range(index_one - (K - 1), index_one + 1):
        right_index = left_index + (K - 1)
        if left_index < 0 or right_index > N - 1:
            continue
        cnt = 1 + math.ceil(left_index / (K - 1)) + math.ceil((N - 1 - right_index) / (K - 1))
        min_cnt = min([min_cnt, cnt])
    print(min_cnt)


if __name__ == '__main__':
    main()