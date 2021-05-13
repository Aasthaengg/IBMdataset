import math as mt
import sys, string
from collections import Counter, defaultdict
input = sys.stdin.readline

MOD = 1000000007

# input functions
I = lambda : int(input())
M = lambda : map(int, input().split())
Ms = lambda : map(str, input().split()) 
ARR = lambda: list(map(int, input().split()))

def main():
    n, k = M()
    arr = ARR()
    for i in range(n - k):
        # print(arr[i], arr[k+i])
        if arr[k + i] > arr[i]:
            print("Yes")
        else:
            print("No")
        


# testcases
tc = 1
for _ in range(tc):
    main()