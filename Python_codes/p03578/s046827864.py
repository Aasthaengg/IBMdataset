N = int(input())
Ds = [int(i) for i in input().split(' ')]
M = int(input())
Ts = [int(i) for i in input().split(' ')]

if M > N:
     print('NO')
else:
    dic = {}
    for d in Ds:
        if d in dic:
            dic[d] += 1
        else:
            dic[d] = 1
    for t in Ts:
        flag = 0
        if t in dic:#存在しているならば
            dic[t] -= 1
            if dic[t] < 0:
                flag = 1
                break
        else:#存在していないならば
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')