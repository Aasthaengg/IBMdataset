import math

MAX_N = 10**6+10

N = int(input())
A = list(map(int,input().split()))
B = [0] * MAX_N
for a in A:
    B[a] += 1

cnt = [0] * MAX_N
for i in range(2,MAX_N):
    for d in range(i, MAX_N, i):
        cnt[i] += B[d]

if N in cnt:
    print("not coprime")
else:
    for c in cnt:
        if c > 1:
            print("setwise coprime")
            exit()
    print("pairwise coprime")