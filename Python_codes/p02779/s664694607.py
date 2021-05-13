import numpy as np
N = int(input())
if N != len(set(list(map(int,input().split())))):
    print("NO")
else:
    print("YES")
