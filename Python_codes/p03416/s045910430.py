a, b = map(int, input().split())

count = 0

for x in range(a, b+1):
    num = str(x)
    if num == num[::-1]:
        count += 1
print(count)
