# -*- coding: utf-8 -*-
# template: v1.2

import io
import sys
import math

def solve(n,k,x,y):
    # implement process
    higher = n-k
    if higher < 1:
        return n*x
    else:
        return k*x + higher*y



def main():
    # input
    n,k,x,y = map(int,sys.stdin.read().split())
    
    # process
    ans = str( solve(n,k,x,y) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
2
3
10000
9000
"""
_EXPECTED = """\
20000
"""

def logd(str):
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