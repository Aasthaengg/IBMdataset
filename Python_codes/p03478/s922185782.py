n, a, b = (int(x) for x in input().split())
result = 0

for num in range(1, n+1):
    res = sum(list(map(int, str(num))))
    if a <= res and res <= b:
        result += num

print(result)
