N = int(input())
A = tuple(map(int, input().split(' ')))
s = 0
for a in A:
    s += 1 / a

print(1 / s)
