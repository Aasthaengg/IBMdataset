a = int(input())
b = int(input())
h = int(input())
area = h * min(a, b) + h * abs(b - a) * 0.5
print(int(area))