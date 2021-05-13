# ABC068 B - Break Number
N = int(input())

for i in range(7):
    if N >= 2**i:
        M = 2**i
print(M)