from heapq import *
import sys
from collections import *

from itertools import *
from decimal import *
import copy
from bisect import *
import time

import math
import datetime
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
sys.setrecursionlimit(10**7)
input=lambda :sys.stdin.readline().rstrip()

N,K=map(int,input().split())
print(K*pow(K-1,N-1))
