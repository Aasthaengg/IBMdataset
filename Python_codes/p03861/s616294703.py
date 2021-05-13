N = list(map(int, input().split()))
a = N[0]
b = N[1]
x = N[2]
if a % x == 0:
    a_min = a // x - 1
else:
    a_min = a // x
b_max = b // x
print(b_max - a_min)