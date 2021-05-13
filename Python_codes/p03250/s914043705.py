A, B, C = map(int, input().split())
num1 = A*10 + B + C
num2 = A + B*10 + C
num3 = A + B + C*10
print(max(num1, num2, num3))