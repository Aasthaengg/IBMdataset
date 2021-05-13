import itertools

A, B, C = map(int, input().split())
number = [A, B, C]
for a,b in itertools.combinations([A,B,C], 2):
    if a == b:
        number.remove(a)
        number.remove(b)
print(number[0])