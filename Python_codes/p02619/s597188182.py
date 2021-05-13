import sys
import math
from collections import deque
from collections import defaultdict
from copy import deepcopy
from itertools import accumulate #リストを与えると累積和を返す
def input(): return sys.stdin.readline().rstrip()
from functools import lru_cache #メモ化
def choice_contest(c, data_day, last, day, contest):
    contest -= 1
    #print(last)
    last = [i + 1 for i in last]
    # 今回開催するコンテストのlastを0にする
    last[contest] = 0
    #print(len(last))
    #print(last)
    # 不満度の計算
    d_satis = sum([last[i] * c[i] for i in range(26)])
    # i日目にcontestを選んだ場合の
    return [int(data_day[contest]) - d_satis, last]

def main():
    d = int(input())
    c = list(map(int,input().split()))
    data = [input().split() for _ in range(d)]
    last = [0] * 26
    ans = 0
    for i in range(d):
        s, last = choice_contest(c, data[i], last, i, contest = int(input()))
        ans += s
        print(ans)
    return 0

if __name__ == "__main__":
    main()