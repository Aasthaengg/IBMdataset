if __name__=="__main__":
    ind = [0, 0, 0, 0]
    for i in range(3):
        x, y = input().split(' ')
        x = int(x);
        y = int(y);
        ind[x - 1] += 1
        ind[y - 1] += 1
    sum = 0;
    for i in ind:
        sum += (i & 1)
    if sum == 0 or sum == 2:
        print('YES')
    else:
        print('NO')