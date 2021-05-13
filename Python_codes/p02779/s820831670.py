# import itertools
# import math
# import sys
import numpy as np

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()


A = np.array(list(map(int, input().split())))

print('YNEOS'[len(A) != len(np.unique(A))::2])