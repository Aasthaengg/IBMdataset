import math
import fractions
import sys
import itertools
import numpy as np
#入力:N(int:整数)
def input1():
	return int(input())

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

def keta(N):
	return len(str(N))

r=input1()
print(r**2)