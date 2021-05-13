H, W = map(int, input().split(' '))
count = [['0']*W for i in range(H)]

def update_count(i, j, count):
    count[i][j] = '#'
    start_i = 0 if i-1 < 0 else i-1
    end_i = H if i + 2 > H else i+2
    start_j = 0 if j-1 < 0 else j-1
    end_j = W if j + 2 > W else j+2
    for k in range(start_i, end_i):
        for l in range(start_j, end_j):
            if count[k][l] != '#':
                count[k][l] = str(1 + int(count[k][l]))
    return count

for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '#':
            count = update_count(i, j, count)

for i in range(H):
    print(''.join(count[i]))
