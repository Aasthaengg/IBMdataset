import math
import copy
import sys
import bisect
input = sys.stdin.readline

def main():
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort()
    c.sort()
    ans=0
    for x in b:
        ans += bisect.bisect_left(a, x) * (n - bisect.bisect_right(c, x))
    print(ans)
if __name__ == "__main__":
    main()