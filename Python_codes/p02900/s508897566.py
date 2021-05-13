# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:11:35 2020

@author: NEC-PCuser
"""
def gcd(a, b):
    
    if (a % b == 0):
        return b
    return gcd(b, a % b)

def factorize(num):
    i = 2
    factorize_list = []
    num_tmp = num
    while i * i <= num_tmp:
        count = 0
        if num % i == 0:
            while num % i == 0:
                count += 1
                num //= i
            factorize_list.append([i, count])
        i += 1
    if num != 1:
        factorize_list.append([num, 1])
    return factorize_list 
                


if __name__ == "__main__":
    A, B =  map(int, input().split())
    big_num = max(A, B)
    short_num = min(A, B)
    gcd_num = gcd(big_num, short_num)
    print(len(factorize(gcd_num)) + 1)
            
