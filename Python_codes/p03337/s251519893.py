A, B = tuple(int(num) for num in input().split())

plus = A + B
mat = A * B
sub = A - B
print(max(plus, mat, sub))