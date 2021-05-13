from math import gcd 
 
n = int(input())
maxA = 10**6+1
A = list(map(int, input().split()))
c = [0]*maxA
for a in A:
    c[a] += 1

for i in range(2, maxA):
    cnt = 0
    for j in range(i, maxA, i):
        cnt += c[j]
    if cnt >= 2:
        break
else:
    print('pairwise coprime')
    exit()

g = A[0]
for a in A[1:]:
    g = gcd(g, a)
if g == 1:
    print('setwise coprime')
else:
    print('not coprime')