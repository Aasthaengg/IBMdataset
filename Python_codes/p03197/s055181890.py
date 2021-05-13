n = int(input())
al = [0] * n
for i in range(n):
    a = int(input())
    if a % 2 != 0:
        print('first')
        break
else:
    print('second')
