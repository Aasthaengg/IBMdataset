n = int(input())
result = ''
for x in range(3, n+1):
    if x % 3 == 0 or '3' in str(x):
        result += (' '+str(x))
print(result)

