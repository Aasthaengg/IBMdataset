#import
#import math
#import numpy as np
#= int(input())
S = input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= {i:[] for i in range(N)}

s = S[0]

r = 0

for i in range(1, len(S)):
    if s != S[i]:
        r += 1

    s = S[i]

print(r)