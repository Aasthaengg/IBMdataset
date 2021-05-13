import math
import fractions


import sys
import itertools
input = sys.stdin.readline
 
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

n = I()
def main():
    for i in range(n):
        temp = I()
        try:
            past = temp * past // fractions.gcd(temp, past)
        except:
            past = temp
    print(past)
    
main()