A, B, C = map(int, input().split())

result = 'Yes' if (A <= C) and (C <= B) else 'No'
print(result)
