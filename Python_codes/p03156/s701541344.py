n = int(input())
a, b = map(int, input().split())
p = [int(_) for _ in input().split()]

num1, num2, num3 = 0, 0, 0
for i in p:
    if i <= a:
        num1 += 1
    elif b+1 <= i:
        num3 += 1
    else:
        num2 += 1
print(min(num1, num2, num3))