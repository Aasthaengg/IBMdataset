A, B = list(map(int, input().split(' ')))
result = A + B if B % A == 0 else B - A
print(result)