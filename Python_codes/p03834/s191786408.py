import sys
import math
import bisect

def main():
    s = list(input())
    for i in range(len(s)):
        if s[i] == ',':
            s[i] = ' '
    print(''.join(s))

if __name__ == "__main__":
    main()
