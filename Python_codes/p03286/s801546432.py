N, re = int(input()), ""
while N != 0:
    re += str(N % 2)
    N = -(N // 2)
print(re[::-1] if re else 0)