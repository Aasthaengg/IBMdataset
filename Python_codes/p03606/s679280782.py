# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():
    N=int(input())
    cnt=0
    for i in range(N):
        l,r=map(int,input().split())
        cnt+=r-l+1
    print(cnt)


resolve()