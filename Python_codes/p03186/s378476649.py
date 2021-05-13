a, b, c = map(int, input().split())
result = 0
if b >= c:
    result = b+c
else:
    result = 2 * b
    b, c = 0, c-b
    if a >= c:
        result = result + c
    else:
        result = result + a + 1
print(result)