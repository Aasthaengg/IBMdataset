#!/usr/bin/env python3
import sys
import math

def main():
    N = int(input())
    T = math.ceil((2*N)**0.5)
    rem = T*(T+1)//2 - N
    if rem > T:
      rem = T*(T-1)//2 - N
      T -= 1
    
    for i in range(T):
        if i+1 != rem:
            print(i+1)

if __name__ == '__main__':
    main()