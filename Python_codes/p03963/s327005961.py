import sys
input = sys.stdin.readline
from collections import *

N, K = map(int, input().split())
print(K*(K-1)**(N-1))
