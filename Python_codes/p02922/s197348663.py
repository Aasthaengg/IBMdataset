A, B = map(int, input().split(' '))

if B == 1:
    cnt = 0
else:
    result = A
    cnt = 1
    while result < B:
        result += A - 1
        cnt += 1
print(cnt)