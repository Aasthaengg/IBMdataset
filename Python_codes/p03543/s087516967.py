import sys
import math
import bisect

def solve(s):
    if len(s) != 4:
        return False
    for i in range(len(s)):
        if i - 2 >= 0 and s[i-2] == s[i] and s[i-1] == s[i]:
            return True
    return False

def main():
    s = input()
    if solve(s):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
