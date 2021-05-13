A, B = map(int,input().split())
ans = [['#' for i in range(100)] for j in range(50)] + [['.' for i in range(100)] for j in range(50)]
for x in range(A-1):
    i = x // 25
    j = 2 * (i % 2) + 4 * (x % 25)
    ans[i][j] = '.'
for x in range(B-1):
    i = 99 - x // 25
    j = 2 * (i % 2) + 4 * (x % 25)
    ans[i][j] = '#'
print(*[100, 100])
for i in range(100):
    print(''.join(ans[i]))