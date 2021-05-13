W, a, b = [int(i) for i in input().split()]
result = 0
if abs(a-b) - W >= 0:
    result = abs(a-b) - W

print(result)