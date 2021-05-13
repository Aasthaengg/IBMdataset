# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(s):
    # implement process
    pass

def main():
    # input
    s = input()
    flag = len(set(s)) == 2 and s.count(s[0]) == 2
    ans = "Yes" if flag else "No"
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
AACD
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