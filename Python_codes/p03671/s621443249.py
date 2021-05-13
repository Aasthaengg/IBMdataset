a, b, c = map(int, input().split())

a_b = a + b
a_c = a + c
b_c = b + c

min_ = a_b
if a_c < min_:
    min_ = a_c
if b_c < min_:
    min_ = b_c

print(min_)