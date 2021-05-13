import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]

if S=='Sunny':
    print('Cloudy')
elif S=='Cloudy':
    print('Rainy')
else:
    print('Sunny')