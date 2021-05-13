# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(n, k, a_lst):
    # implement process
    a_set = set(a_lst)
    ak = len(a_set)
    diff = ak - k
    if diff < 1:
        return 0
    
    #ソート済み配列を検査することで、count処理を線形にする
    a_lst.sort()
    tmp = a_lst[0]
    cnt = 0
    cnt_lst = []
    for i in range(len(a_lst)):
        if tmp != a_lst[i]:
            tmp = a_lst[i]
            cnt_lst.append(cnt)
            cnt = 0
        cnt += 1
    cnt_lst.append(cnt)
    cnt_lst.sort()
    return sum(cnt_lst[0:diff])

def main():
    # input
    n, k = map(int,input().split())
    a_lst = list(map(int,input().split()))

    # process
    ans = str( solve(n, k, a_lst) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
5 2
1 1 2 2 5
"""
_EXPECTED = """\
0
"""

def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB: print(f"[deb] {str}")

### MAIN ###
if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")