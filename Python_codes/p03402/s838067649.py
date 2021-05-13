A, B = map(int, input().split())
lst = [['#' for j in range(100)] for i in range(50)] + [['.' for j in range(100)] for i in range(50)]
for i in range(A-1):
    a, b = divmod(i, 50)
    lst[a*2][b*2] = '.'
for i in range(B-1):
    a, b = divmod(i, 50)
    lst[-1-a*2][-1-b*2] = '#'
print(100, 100)
for j in lst:
    print(''.join(j))