import sys
import math
import bisect

def main():
    s = list(input())
    for i in range(len(s)):
        if s[i] == '1':
            s[i] = '9'
        elif s[i] == '9':
            s[i] = '1'
    print(''.join(s))

if __name__ == "__main__":
    main()
