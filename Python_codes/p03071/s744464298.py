a, b = map(int,input().split())
number = 0
if a >= b:
    number += a
    number += max(a-1, b)
else:
    number += 2 * b - 1
print(number)