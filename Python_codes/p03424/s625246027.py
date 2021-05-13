N = int(input())

Sn = input().split()

for c in Sn:
    if c == 'Y':
        num = 1
        break
    num = 0

if num == 1:
    result = 'Four'
else:
    result = 'Three'

print(result)
