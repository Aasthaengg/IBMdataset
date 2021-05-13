# -*-coding: utf-8 -*-

import sys
import math

def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a % b)

def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    input = sys.stdin.readline
    a, b, c, d = map(int, input().split())
    a_1 = a - 1
    lcm_cd = lcm(c,d)
    
    a_1_c_count =  a_1 // c
    a_1_d_count =  a_1 // d
    a_lcm_count =  a_1 // lcm_cd

    a_1_result = a_1 - (a_1_c_count + a_1_d_count - a_lcm_count)


    b_c_count = b // c
    b_d_count = b // d
    b_lcm_count = b // lcm_cd

    b_result = (b) - (b_c_count + b_d_count - b_lcm_count)

    result = b_result - a_1_result

    print(result)
    return


if __name__ == '__main__':
    main()