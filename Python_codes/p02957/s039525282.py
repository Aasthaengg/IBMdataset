a, b = list(map(int, input().rstrip().split()))
k = abs(a - b) / 2
result = 'IMPOSSIBLE'
if float.is_integer(k):
    result = str(int(min(a, b) + k))

print(result)