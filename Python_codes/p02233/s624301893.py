# -*- coding: utf-8 -*-
 
 
def main(n):
    lst = [1, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 2] + lst[i - 1])
    return lst[n]
 

if __name__ == '__main__': 
    n = int(input())
    print(main(n))