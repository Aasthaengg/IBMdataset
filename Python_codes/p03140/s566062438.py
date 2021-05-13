n = int(input())
a = str(input())
b = str(input())
c = str(input())
result = 0
for i in range(n):
    counter = 1
    if a[i] == b[i]:
        counter += 1
    if a[i] == c[i]:
        counter += 1
    elif b[i] == c[i]:
        counter += 1
    result += abs(3-counter)
print(result)