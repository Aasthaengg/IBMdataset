n = int(input())

result = []
for i in range(n):
    a = i + 1
    if a % 3 != 0 and a % 5 != 0:
        result.append(a)
print(sum(result))
