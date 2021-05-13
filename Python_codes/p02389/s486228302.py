a, b = map(int, input().split())

if 1 <= a <= 100 and 1 <= b <= 100:
    area = a * b
    perimeter = (a + b) * 2
    print(area, perimeter)
