n = int(input())
A = [int(x) for x in input().split()]
comp = 0
for el in range(0, n, 2):
    if A[el] % 2 != 0:
        comp += 1

print(comp)