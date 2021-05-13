# coding: utf-8
# Your code here!
import math

def main():
    a, b, c, k = map(int, input().split())
    if k >= a:
        ans = a
        k = k - a
    else:
        print(k)
        return 0
    if k >= b:
        k = k - b
    else:
        print(ans)
        return 0
    if k >= c:
        ans -= c
    else:
        ans -= k
    print(ans)
    
    
main()