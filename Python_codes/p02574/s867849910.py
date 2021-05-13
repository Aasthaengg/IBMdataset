import sys, math

N = int(input())
A = list(map(int, input().split()))
G = 0
for a in A:
    G = math.gcd(G, a)

if G != 1:
    print("not coprime")
    exit(0)

M = 10 ** 6 + 5
B = dict()
for a in A:
    if a in B:
        B[a] = B[a] + 1
    else:
        B[a] = 1

for i in range(2, M):
    cnt = 0
    for j in range(i, M, i):
        if j in B:
            cnt += B[j]
    if cnt > 1:
        print("setwise coprime")
        exit(0)

print("pairwise coprime")
