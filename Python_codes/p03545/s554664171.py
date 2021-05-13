num = str(input())
op = ['+', '-']

for i in range(2**3):
    ans = int(num[0])
    t_op = []
    for j in range(3):
        if (i >> j)&1:
            ans -= int(num[j+1])
            t_op.append('-')
        else:
            ans += int(num[j+1])
            t_op.append('+')
    if ans == 7:
        ans_l = [num[0], t_op[0], num[1], t_op[1], num[2], t_op[2], num[3], '=7']
        print(*ans_l,sep='')
        break