import itertools
import math

antena = []
antena.append(int(input()))
antena.append(int(input()))
antena.append(int(input()))
antena.append(int(input()))
antena.append(int(input()))
k = int(input())
for v in itertools.combinations(antena, 2):
    if v[1] - v[0] > k:
        print(":(")
        quit()
print('Yay!')