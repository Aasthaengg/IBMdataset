A, B, C = input().split()
num = sorted([A, B, C], reverse=True)
num1 = int(''.join(num)[:2])
num2 = int(num[2])
print(num1+num2)