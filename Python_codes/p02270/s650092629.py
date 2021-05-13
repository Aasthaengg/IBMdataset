import sys

global n, k, T


def cal_v(P):
    j = 0
    for i in range(k):
        con = 0
        while con + T[j] <= P:
            con += T[j]
            j += 1
            if j == n:
                return n
    return j


def cal_ans():
    left = 0
    right = sum(T)
    mid = (right-left) // 2
    while right - left > 1:
        mid = left + (right-left)//2
        if cal_v(mid) >= n:
            right = mid
        else:
            left = mid
    return right

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    T = list(map(int, sys.stdin.readlines()))
    ans = cal_ans()
    print(ans)