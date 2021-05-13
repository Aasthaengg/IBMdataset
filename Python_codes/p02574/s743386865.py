import numpy as np
n = int(input())
a = list(map(int, input().split()))
g = np.gcd.reduce(a)

if g > 1:
    print("not coprime")
    exit()

c = [0]*(10**6 + 1)

for i in a:
    c[i] += 1

for i in range(2, 10**6 + 1):
    if sum(c[i::i]) > 1:
        print("setwise coprime")
        exit()

print("pairwise coprime")