import sys
input = sys.stdin.readline
from collections import *

P, Q, R = map(int, input().split())
print(min(P+Q, Q+R, R+P))