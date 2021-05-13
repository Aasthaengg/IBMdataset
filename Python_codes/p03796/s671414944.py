#-*-coding:utf-8-*-

import math

def main():
    n = int(input())
    ans =math.factorial(n)
    print(ans%1000000007)

if __name__=="__main__":
    main()