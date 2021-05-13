import sys
from operator import itemgetter
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    N, M = map(int, input().rstrip().split())

    require_list = []
    for _ in range(M):
        s, e = map(int, input().rstrip().split())
        require_list.append([s, e])
    require_list.sort(key=itemgetter(1))

    count = 1
    now_require = require_list[0]
    for next_require in require_list[1:]:
        # 前回の終点よりも、今回の始点の方が右にある場合
        if now_require[1] <= next_require[0]:
            count += 1
        else:
            next_require[1] = now_require[1]
        now_require = next_require

    print(count)

if __name__ == '__main__':
    main()