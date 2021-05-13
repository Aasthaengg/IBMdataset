# coding: utf-8
# Your code here!
import math

def main():
    x, y = map(int, input().split())
    b = (y - 2 * x) / 2
    a = x - b
    if a >= 0 and b >= 0 and a == int(a) and b == int(b):
        print('Yes')
    else:
        print('No')
    
main()