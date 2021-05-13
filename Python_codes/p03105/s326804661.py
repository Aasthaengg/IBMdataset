a,b,c = map(int,(input().split()))

result = b // a
if result > c:
    result = c

print(result)