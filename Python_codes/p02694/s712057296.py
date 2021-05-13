# coding: utf-8
import math
def main():
    x = int(input())
    
    money = 100
    i = 0
    while money < x:
        i += 1
        money = money * 101 // 100
    
    print(i)
    
main()