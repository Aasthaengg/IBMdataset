#import sys
import numpy as np
#from collections import defaultdict
#import math
#from collections import deque

#input = sys.stdin.readline
#import decimal

def main():
    N = int(input())
    S = input()
    S_new =""
    for i in range(len(S)):
         S_new +=chr((ord(S[i])+N-ord("A"))%26+ord("A"))
    print(S_new)
if __name__ == "__main__":
    main()