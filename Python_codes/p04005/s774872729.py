A, B, C = map(int, input().split())

for num in [A, B, C]:
    if num % 2 == 0:
        print(0)
        break
else:
    print(min(A * B, B * C, C * A))