# -*- coding: utf-8 -*-
import io
import sys
import math

def format_multi_answer(lst):
    ans = ""
    ans += f"{len(lst)}\n"
    for y in lst:
        ans += f"{y[0]} {y[1]}\n"
    return ans

def is_condition_ok(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def solve(n,a_lst):
    """
    D_2: 記述軽く、アルゴリズムやや悪い？バージョン
    """
    # implement process
    if is_condition_ok(a_lst):
        return 0

    # get max / min value and index
    i_max, a_max = -1,-1
    i_min, a_min = +1,+1
    for i in range(len(a_lst)):
        if a_max < a_lst[i]:
            a_max = a_lst[i]
            i_max = i
        if a_min > a_lst[i]:
            a_min = a_lst[i]
            i_min = i

    ans_lst = []
    if a_max >= 0 and a_max >= abs(a_min):
        # 全ての負の値にmax値を足し込み正の値にする。次に、plus時の処理を行う。
        if _DEB: logd(f"plus")
        for i in range(len(a_lst)):
            if a_lst[i] < 0:
                ans_lst.append([i_max+1,i+1])
        ans_lst.append([i_max+1,1])
        for i in range(len(a_lst)-1):
            ans_lst.append([i+1,i+2])
    else:
        # 全ての正の値を負の値にし、minus時の処理を行う。
        if _DEB: logd(f"minus")
        for i in range(len(a_lst)):
            if a_lst[i] >= 0:
                ans_lst.append([i_min+1,i+1])
        ans_lst.append([i_min+1,len(a_lst)])
        for i in range(len(a_lst)-1,0,-1):
            ans_lst.append([i+1,i])

    return format_multi_answer(ans_lst)

def main():
    # input
    n = int(input())
    a_lst = list(map(int, input().split()))

    # process
    ans = str( solve(n,a_lst) ).strip()
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
2
-1 -3
"""
_EXPECTED = """\
2
2 3
3 3
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