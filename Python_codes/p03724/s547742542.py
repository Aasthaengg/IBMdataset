n,m = map(int,input().split())
ab = [[int(i) for i in input().split()] for j in range(m)]

im_b = [0]*(n)

for i in range(m):
    im_b[ab[i][0]-1] += 1
    im_b[ab[i][1]-1] -= 1

if im_b[0] % 2 == 1:
    print('NO')
    exit()

#im_a = [0]*(n)
#im_a[0] = im_b[0]

for i in range(n-1):
    #print(i)
    if im_b[i] % 2 == 1:
        print('NO')
        exit()

print('YES')