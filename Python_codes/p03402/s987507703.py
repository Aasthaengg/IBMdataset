a,b = map(int,input().split())
grid_b = [list('#'*100) for _ in range(50)]
grid_w = [list('.'*100) for _ in range(50)]
for i in range(a-1):
    grid_b[2*(i//50)+1][2*(i%50)+1] = '.'
for i in range(b-1):
    grid_w[2*(i//50)+1][2*(i%50)+1] = '#'
print(100, 100)
for i in range(50):
    print(''.join(grid_b[i]))
for i in range(50):
    print(''.join(grid_w[i]))