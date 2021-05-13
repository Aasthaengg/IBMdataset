import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import gcd
def main():
    n, m = map(int, input().split())
    s = tuple(input())
    t = tuple(input())

    if n > m:
        l1 = n
        l2 = m
        s1 = s
        s2 = t
    else:
        l1 = m
        l2 = n
        s1 = t
        s2 = s

    if s[0] != t[0]:
        r = -1
    elif n == m:
        if s == t:
            r = n
        else:
            r = -1
    elif n % m == 0 or m % n == 0:
        ld = l1 // l2
        for i1 in range(1, l2):
            if s2[i1] != s1[i1*ld]:
                r = -1
                break
        else:
            r = l1
    else:
        l = (n * m) // gcd(n, m)
        # x = [0] * l
        ld1 = l // l1
        ld2 = l // l2
        cnt = 1
        r = l
        while cnt < l1:
            cnt2 = cnt * ld1
            if cnt2 % ld2 == 0:
                if s1[cnt] != s2[cnt2 // ld2]:
                    r = -1
                    break
            cnt += 1
    print(r)

if __name__ == '__main__':
    main()