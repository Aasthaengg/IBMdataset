import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
from bisect import bisect
def main():
    s = input()
    k = int(input())
    s2 = []
    s2a = s2.append
    for se in s:
        if ord(se) - 97:
            s2a(123 - ord(se))
        else:
            s2a(0)
    s2_ac = tuple(accumulate(s2))
    lens = len(s)
    if s2_ac[-1] < k:
        k -= s2_ac[-1]
        k = k % 26
        r = 'a' * (lens - 1) + chr(97 + k)
        print(r)
    elif s2_ac[-1] == k:
        r = 'a' * lens
        print(r)
    else:
        pos = bisect(s2_ac, k)
        if pos == 0:
            r = chr(k + ord(s[0])) + s[1:]
            print(r)
        elif s2_ac[pos-1] == k:
            r = 'a' * pos + s[pos:]
            print(r)
        else:
            r = 'a' * pos
            k -= s2_ac[pos-1]
            for i1 in range(pos, len(s)):
                if s2[i1] <= k:
                    r += 'a'
                    k -= s2[i1]
                else:
                    r += s[i1]
            if k:
                lastc = chr(ord(r[-1]) + k)
                r = r[:-1] + lastc
            print(r)

if __name__ == '__main__':
    main()