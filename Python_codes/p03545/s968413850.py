num_li = list(input())
for i in range(2**3):
    li = ['+']*3
    q = num_li[0]
    for j in range(3):
        if ((i>>j) & 1):
            li[j] = '-'
        q += li[j] + num_li[j+1]
    if eval(q) == 7:
        print('{}=7'.format(q))
        break