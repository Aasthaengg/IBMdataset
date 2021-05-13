lis = [list(map(int, input().split())) for _ in range(3)]

n = [0]*4

for i in lis:
    n[i[0]-1] += 1
    n[i[1]-1] += 1

for j in n:
    if j >=3 or j ==0:
        print('NO')
        exit()
print('YES')