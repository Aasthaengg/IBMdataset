#B - Problem Set

# -*- coding: utf-8 -*-
from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

D_count = Counter(D)
T_count = Counter(T)

for t_key, t_val in T_count.items():
    if(t_key in D_count):
        if(t_val > D_count[t_key]):
            print("NO") 
            exit()
    else:
        print("NO")
        exit()

print("YES")