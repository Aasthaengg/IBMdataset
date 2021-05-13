A,B = map(int,input().split())

H = W = 100
ans = [['.#'[i//50]]*W for i in range(H)]

A -= 1
B -= 1

i = j = 0
while B:
    ans[i][j] = '#'
    j += 2
    if j >= W:
        j = 0
        i += 2
    B -= 1

i = 52
j = 0
while A:
    ans[i][j] = '.'
    j += 2
    if j >= W:
        j = 0
        i += 2
    A -= 1

print(H,W)
for row in ans:
    print(''.join(row))