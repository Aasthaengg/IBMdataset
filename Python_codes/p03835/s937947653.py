#import
#import math
#import numpy as np
#= int(input())
#= input()
K, S = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= {i:[] for i in range(N)}

r = 0

for i in range(K + 1):
    for j in range(K + 1):
        z = S - (i + j)
        if z >= 0 and z <= K:
            r += 1

print(r)