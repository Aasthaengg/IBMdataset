import math

S = input()
w = int(input())

a = ''
for s in range(math.ceil(len(S) / w)):
    a += S[s*w]

print(a)


