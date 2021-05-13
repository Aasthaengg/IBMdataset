A, B = map(int, input().split())

sum = A + B
sub = A - B
mul = A * B

print(max([sum, sub, mul]))