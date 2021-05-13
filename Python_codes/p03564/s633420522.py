n = int(input())
k = int(input())
result = 1
for i in range(n):
    if result*2 > result+k:
        result += k
    else:
        result += result

print(result)