N = [int(x) for x in input().split(' ')]
N = sorted(N)

ans_list = [N[0]] + sorted(N[1:4], reverse = True)
ans = ''.join(map(str, ans_list))

if ans == '1974':
    print('YES')
else:
    print('NO')