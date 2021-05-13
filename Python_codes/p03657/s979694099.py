a, b = map(int, input().split())
data = [a, b, a+b]
flag = 'Impossible'
for d in data:
    if d % 3 == 0:
        flag = 'Possible'
print(flag)