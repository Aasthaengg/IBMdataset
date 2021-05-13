# coding: utf-8
# Your code here!
import math

def main():
    a, b, h, m = map(int, input().split())
    arg_a = 360 * (h * 60 + m) / (12 * 60)
    arg_b = 360 * m / 60
    arg = min(abs(arg_a - arg_b), 360 - abs(arg_a - arg_b))
    # print(arg)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(arg)))
    
    print(c)
    
main()