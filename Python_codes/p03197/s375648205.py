n = int(input())
flag = True
for _ in range(n):
    i = int(input())
    if i%2 == 1:
        print('first')
        exit()
print('second')