n = int(input())
a = int(input())

can_pay = True if n - 500 * (n // 500) <= a else False
print("Yes" if can_pay else "No")
