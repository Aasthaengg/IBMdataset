import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    # 0を左端、N-1を右端として二分探索を行う
    print(0)
    left_response = input()
    if left_response == "Vacant":
        exit()

    print(n - 1)
    right_response = input()
    if right_response == "Vacant":
        exit()

    left = 0
    right = n - 1

    for i in range(20):
        mid = (left + right) // 2
        print(mid)
        mid_response = input()

        if mid_response == "Vacant":
            exit()

        if (mid - left) % 2 == 0 and left_response == mid_response:
            left = mid
            left_response = mid_response
        elif (mid - left) % 2 == 1 and left_response != mid_response:
            left = mid
            left_response = mid_response
        else:
            right = mid
            right_response = mid_response


if __name__ == '__main__':
    resolve()
