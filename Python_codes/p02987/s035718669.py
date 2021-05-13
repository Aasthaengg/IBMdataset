# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(s):
    # implement process
    a,b = "",""
    cnt = 0
    # process
    for c in s:
        if a == "":
            a = c
            cnt += 1
        elif a == c:
            cnt += 1
        elif b == "":
            b = c
        elif b != c:
            return False
    return cnt == 2

def main():
    # input
    s = input()

    ans = "Yes" if solve(s) else "No"
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
FFEE
"""
_EXPECTED = """\
Yes
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