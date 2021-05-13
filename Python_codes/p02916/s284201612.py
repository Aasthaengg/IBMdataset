# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(n, a_lst,b_lst,c_lst):
    # implement process
    pre_a = -float('inf')
    satisfaction = 0
    for a in a_lst:
        a -= 1
        satisfaction += b_lst[a]
        if pre_a +1 == a:
            satisfaction += c_lst[a-1]
        pre_a = a
    
    return satisfaction
    
def main():
    # input
    n = int(input())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    c_lst = list(map(int, input().split()))

    # process
    ans = str( solve(n, a_lst,b_lst,c_lst ) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
2
1 2
50 50
50
"""
_EXPECTED = """\
150
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