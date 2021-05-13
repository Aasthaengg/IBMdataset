from itertools import accumulate
N, Q = map(int,input().split())
S = input()
AC = [0]*N
flag = 0
for idx, s in enumerate(S):
    if flag and s == "C":
        AC[idx] = 1
    if s == "A":
        flag = 1
    else:
        flag = 0

acc = list(accumulate(AC))

for i in range(Q):
    l, r = map(int,input().split())
    print(acc[r-1]-acc[l-1])