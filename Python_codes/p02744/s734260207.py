# coding: utf-8
# Your code here!
from sys import stdin
import numpy as np
#import math
#from functools import reduce
    
#N, M = [int(x) for x in stdin.readline().rstrip().split()]
N = int(input())
#S = list(input())

def append_str(W, N):
    w_new = []
    for w in W:
        kind = len(set(w))
        for i in range(kind+1):
            w_new.append(w+alphabets[i])
    return w_new
    

seed = 'a'
alphabets = ['a', 'b','c','d','e','f','g','h','i','j']

#長さNの文字列に含まれる文字の種類はN以下
for n in range(N):
    if n == 0:
        w = [seed]
    else:
        w = append_str(w, n+1)
    
for buf in w:
    print(buf)