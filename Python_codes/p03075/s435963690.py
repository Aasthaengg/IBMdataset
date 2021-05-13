from itertools import combinations

A = [int(input()) for _ in range(5)]
k = int(input())
for a in combinations(A, 2):
    p, q = a
    if abs(p - q) > k:
        print(":(")
        exit()
print("Yay!")
