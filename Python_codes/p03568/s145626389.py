import numpy as np


def main():
    length = int(input())
    sequence = list(map(int, input().split()))
    answer = 0
    for i in range(3 ** length):
        ternary_i = np.base_repr(i, 3).zfill(length)
        now_product = 1
        for j in range(length):
            if ternary_i[j] == "0":
                now_product *= sequence[j]
            elif ternary_i[j] == "1":
                now_product *= sequence[j] + 1
            else:
                now_product *= sequence[j] - 1
        if now_product % 2 == 0:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()

