import sys
import math
import itertools
#n=int(input())
n, k = map(int, input().split())
print(k*((k-1)**(n-1)))