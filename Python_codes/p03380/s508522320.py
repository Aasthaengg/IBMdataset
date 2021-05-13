# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:55:07 2020

@author: NEC-PCuser
"""

def binary_search(b, a):
    low = 0
    high = len(b) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = b[mid]
        if guess == a:
            return b[mid]
        elif guess > a:
            high = mid - 1
        else:
            low = mid + 1
    abs_low = a * 4
    if len(b) > low: 
        abs_low = abs(b[low] - a)
    abs_high = abs(b[high] - a)
    return b[high] if abs_low > abs_high else b[low]
    
            


if __name__ == "__main__":
    n = int(input())
    
    a = list(map(int, input().split()))
    
    a.sort()
    
    b = a[0:len(a)-1]
    c = binary_search(b, a[len(a)-1] / 2)
    print(str(a[len(a)-1]) + " " + str(c))