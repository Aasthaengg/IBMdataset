N, M = map(int, input().split())
ls = []
for i in range(M):
    p, y = map(int, input().split())
    ls.append([i, p, y])
ls.append([float('inf'), float('inf'), 1])
ls.sort(key=lambda x: x[1])
rem = []
ans = []
cur_p = -1
for i in range(M+1):
    if ls[i][1] == float('inf'):
        rem.sort(key=lambda x: x[2])
        for j in range(len(rem)):
            rem_j = rem[j][:]
            rem_j.append('0'*(6-len(str(rem_j[1]))) + str(rem_j[1]) + '0'*(6-len(str(j+1))) + str(j+1))
            ans.append(rem_j)
        break
    if cur_p != ls[i][1]:
        if len(rem) != 0:
            rem.sort(key=lambda x: x[2])
            for j in range(len(rem)):
                rem_j = rem[j][:]
                rem_j.append('0'*(6-len(str(rem_j[1]))) + str(rem_j[1]) + '0'*(6-len(str(j+1))) + str(j+1))
                ans.append(rem_j)
            cur_p = ls[i][1]
            rem = []
            rem.append(ls[i])
        else:
            rem.append(ls[i])
            cur_p = ls[i][1]
    else:
        rem.append(ls[i])
ans.sort(key=lambda x: x[0])
for x in ans:
    print(x[-1])