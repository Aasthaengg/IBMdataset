import sys,math
import numpy as np
input = sys.stdin.readline

b_max=0
a_max=0
a = []
b = []
N,H = list(map(int,input().split()))
for i in range(N):
    an,bn = list(map(int,input().split()))
    a.append(an)
    b.append(bn)
    a_max = max(a_max,an)
    b_max = max(b_max,bn)
a = np.array(a)
b = np.array(b)
b = sorted(list(b[b>=a_max]))

cnt = 0
for i in range(len(b)):
    H -= b.pop()
    cnt += 1
    if H <=0:
        print(cnt)
        exit()

cnt += math.ceil(H/a_max)
print(cnt)
