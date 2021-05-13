n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        continue
    print('first')
    break
else:
    print('second')
