a, b, c = map(int, input().split())
 
result = 'Yes' if (a <= c) and (c <= b) else 'No'
print(result)