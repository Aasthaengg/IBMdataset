n = int(input())
left = 0
right = n - 1
print(left)
first = input()
second = 'Male' if first == 'Female' else 'Female'
p = 0
while True:
    p = (left + right) // 2
    print(p)
    status = input()
    if status == 'Vacant':
        break
    if p % 2 == 0:
        if status == first:
            left = p + 1
        else:
            right = p
    else:
        if status == second:
            left = p + 1
        else:
            right = p