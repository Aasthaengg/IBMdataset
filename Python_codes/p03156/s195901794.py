n = int(input())
a, b = map(int, input().split())
p = sorted(list(map(int, input().split())))

num1 = len([x for x in p if x <= a])
num2 = len([x for x in p if a < x <= b])
num3 = len([x for x in p if b < x])

print(min(num1, num2, num3))