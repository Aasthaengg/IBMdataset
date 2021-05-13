a, b, c = map(int, input().split())
result = b
if b+a<c:
    result += a+b+1
else:
    result += c
print(result)