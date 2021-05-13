# import sys
# input = sys.stdin.readline
import itertools


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n, k = input_list()
    a = input_list()
    kitais = [0]
    for i in range(n):
        kitai = (a[i]+1)/2
        kitais.append(kitais[i] + kitai)
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, kitais[i+k] - kitais[i])
    print(ans)

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
