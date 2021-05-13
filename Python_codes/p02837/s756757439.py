n = int(input())

remark_list = [[] for _ in range(n)] # -1:言及なし, 0:不親切, 1：親切
for i in range(n):
    a = int(input())
    for j in range(a):
        remark_list[i].append(list(map(int, input().split())))

ans = 0
for i in range(2**n):
    state = [-1]*n
    is_ok = True
    ok_num = 0
    for j in range(n):
        if ((i >> j) & 1):
            if state[j] != 0:
                state[j] = 1
            else:
                is_ok = False
            remark = remark_list[j]
            ok_num += 1
            for r in remark:
                if state[r[0]-1] == -1:
                    state[r[0]-1] = r[1]
                elif state[r[0]-1] != r[1]:
                    is_ok = False
                    break
        else:
            if state[j] != 1:
                state[j] = 0
            else:
                is_ok = False
    if is_ok:
        ans = max(ans, ok_num)
print(ans)
