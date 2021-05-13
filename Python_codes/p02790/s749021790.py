
(a, b) = tuple(map(int, input().split()))

str_a = str(a) * b
str_b = str(b) * a
print(sorted([str_a, str_b])[0])