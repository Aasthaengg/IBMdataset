n = int(input())
C = {}
for _ in range(n):
    a = input()
    if a not in C:
        C[a] = 0
    C[a] += 1
for i in C.keys():
    C[i] %= 2
print(sum(C.values()))