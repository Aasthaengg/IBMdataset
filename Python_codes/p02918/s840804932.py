#!/usr/bin/env python3
import sys
from itertools import groupby

# RUN LENGTH ENCODING
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, str(len(list(v)))))
    return res

def runLengthdecode(L: "list[tuple]"):
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, K = map(int, input().split())
    S = input()
    compressed = runLengthEncode(S)

    # ある区間を反転させるとその両端が前後で連結するようにするのが最大化できる = 両端の操作は損
    for k in range(K):
        i = 2 * k + 1   # 奇数インデックスのみ反転させる。
        if i >= len(compressed):
            break
        compressed[i] = ('L', compressed[i][1]) if compressed[i][0] == "R" else ('R', compressed[i][1])

    reCompressed = runLengthEncode(runLengthdecode(compressed))
    ans = N - len(reCompressed)

    print(ans)

if __name__ == '__main__':
    main()