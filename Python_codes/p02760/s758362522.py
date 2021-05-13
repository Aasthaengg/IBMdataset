al=[list(map(int, input().split())) for _ in range(3)]
bl=[[False]*3 for _ in range(3)]
n=int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if al[i][j] == b: bl[i][j] = True

for i in range(3):
    if all(bl[i]):
        print('Yes')
        exit()

for j in range(3):
    if all([bl[0][j],bl[1][j],bl[2][j]]):
        print('Yes')
        exit()

if all([bl[0][0],bl[1][1],bl[2][2]]) or all([bl[2][0],bl[1][1],bl[0][2]]):
    print('Yes')
    exit()

print('No')