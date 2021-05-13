import sys
input=sys.stdin.readline

import collections

def main():
    A = input().strip()
    n = len(A)
    ans = 1 + n*(n-1)//2
    for k in collections.Counter(A).values():
        ans -= k*(k-1)//2
    print(ans)

if __name__ == '__main__':
    main()
