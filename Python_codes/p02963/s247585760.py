S = int(input())
MAX_V = 10 ** 9
X3 = -S % MAX_V
Y3 = (S + X3) // MAX_V
print(0, 0, MAX_V, 1, X3, Y3)
