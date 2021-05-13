a, b = map(int, input().split())
# masu = ['#' for _ in range(10000)]
masu = [['#' for _ in range(100)] for _ in range(100)]
for i in range(50, 100):
    for j in range(100):
        masu[i][j] = '.'
cnta = 0
for i in range(0, 50):
    for j in range(99):
        if cnta < a-1 and j % 3 == 1:
            masu[i][j+i % 2] = '.'
            cnta += 1
cntb = 0
for i in range(51, 100):
    for j in range(99):
        if cntb < b-1 and j % 3 == 1:
            masu[i][j+i % 2] = '#'
            cntb += 1

print('100 100')
for i in range(100):
    for j in range(100):
        print(masu[i][j], end='')
    print('')
