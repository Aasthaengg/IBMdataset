# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(ac_lst,l,r):
    # implement process
    #l=2,r=3
    if l == 1:
        return ac_lst[r-2]
    return ac_lst[r-2] - ac_lst[l-2]
    

def make_ac_lst(s):
    ac_lst = [0] * len(s)
    for i in range(len(s)-1):
        if i != 0:
            ac_lst[i] += ac_lst[i-1]
        if s[i] == "A" and s[i+1] == "C":
            ac_lst[i] += 1
    ac_lst[-1] = ac_lst[-2]

    if _DEB: logd(f"{ac_lst}")
    return ac_lst

def main():
    # input
    n,q = map(int, input().split())
    s = input()
    
    # process
    ans = ""
    ac_lst = make_ac_lst(s)

    for _ in range(q):
        l,r = map(int, input().split())
        ans += str( solve(ac_lst,l,r) ) + "\n"
         
    # output    
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
8 3
ACACTAAC
7 8
2 3
1 8
"""
_EXPECTED = """\
2
0
3

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