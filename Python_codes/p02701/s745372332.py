# -*- coding: utf-8 -*-

import io
import sys
import math

def solve():
    # implement process
    pass

def main():
    # input
    n = int(input())
    s_list = []
    for s in range(n):
      s_list.append(input())
    
    # process
    s_set = set(s_list)
    ans = str( len( s_set) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
5
grape
grape
grape
grape
grape
"""
_EXPECTED = """\
1
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