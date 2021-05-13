import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    x, k, d = map(int, input().split())
    cycle = abs(x) // d     # cycle:距離ｘを距離ｄ移動で詰めるための必要移動回数。
    if cycle >= k:          # xまでの移動でｋが尽きる場合。
        print(abs(abs(x) - k * d))
    else:                   # xまで移動してｋが余る場合。
        k -= cycle          # ｋ＝余る移動回数、にする
        if k&1:             # kが奇数なら「ｘを飛び越えた地点」に留まるのが最適解。
            print(abs(abs(x) - (cycle + 1) * d))
        else:
            print(abs(abs(x) - (cycle) * d))

if __name__ == '__main__':
    main()