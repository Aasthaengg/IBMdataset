A, B = map(int, input().rstrip().split(' '))
if B % A == 0:
    result = A + B
else:
    result = B - A

print(result)

