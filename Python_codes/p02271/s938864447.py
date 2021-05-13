from typing import List


def rec(i: int, tmp_sum: int, A_list: List[int], sum_list: List[bool]):
    if tmp_sum > 2000:
        return
    elif i == len(A_list):
        sum_list[tmp_sum] = True
        return

    rec(i + 1, tmp_sum + A_list[i], A_list, sum_list)
    rec(i + 1, tmp_sum, A_list, sum_list)


def main():
    n = int(input())
    A_list = list(map(int, input().split()))
    q = int(input())
    m_list = list(map(int, input().split()))

    sum_list = [False for _ in range(2001)]

    rec(0, 0, A_list, sum_list)

    for m in m_list:
        if sum_list[m]:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()

