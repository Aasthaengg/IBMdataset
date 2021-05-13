import sys
input = sys.stdin.readline
import math


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    s = str(input()).strip()
    n = len(s)
    cnt = 0
    ans = [0] * n
    for i, moji in enumerate(s):
        if moji == "R":
            cnt += 1
            continue
        else:
            even_num = cnt//2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i-1] += odd_num
            cnt = 0
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] == "L":
            cnt += 1
            continue
        else:
            even_num = cnt // 2
            odd_num = cnt - even_num
            ans[i] += even_num
            ans[i+1] += odd_num
            cnt = 0
    print(*ans)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
