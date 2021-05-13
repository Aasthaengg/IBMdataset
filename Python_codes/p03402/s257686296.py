# D - Grid Components

A, B = map(int, input().split())
A -= 1
B -= 1
grid = [['#'] * 100 for _ in range(50)]
grid.extend([['.'] * 100 for _ in range(50)])

for i in range(1, A+1):
    tmp_q = (i * 2) - 1
    q = tmp_q % 100
    tmp_p = tmp_q // 100 + 1
    p = (tmp_p * 2) - 1
    grid[p][q] = '.'

for j in range(1, B+1):
    tmp_q = (j * 2) - 1
    q = tmp_q % 100
    tmp_p = tmp_q // 100 + 1
    p = (tmp_p * 2) - 1
    p += 50
    grid[p][q] = '#'

print('100 100')

for i in range(100):
    print(''.join(map(str, grid[i])))