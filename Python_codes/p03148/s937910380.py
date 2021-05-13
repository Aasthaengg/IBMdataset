N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]
TD += [[0, 0]]
TD.sort(key = lambda x: x[1], reverse = True)
TD.sort(key = lambda x: x[0]) #ネタの種類、おいしさを、ネタの種類でソート

lst = []
for i in range(1, N + 1):
    if TD[i-1][0] != TD[i][0]:
        lst += [[TD[i][1], 1]]
    else:
        lst += [[TD[i][1], 0]]

lst.sort(key = lambda x: x[1], reverse = True)
lst.sort(key = lambda x: x[0], reverse = True)
# print (lst)

total = 0
kind = 0
lst2 = []
for i in range(K):
    total += lst[i][0]
    if lst[i][1] == 1:
        kind += 1
    else:
        lst2 += [lst[i][0]]

ans = total + kind * kind
# print (total, ans)
# print (lst2)
n = len(lst2)
j = K
for i in range(n):
    flag = True
    while flag:
        if j >= N:
            print (ans)
            exit()
        if lst[j][1] == 1: #ネタの種類が増えるものだけ考える
            # print (lst[j])
            total += lst[j][0]
            kind += 1
            # print (lst2[n-1-i])
            total -= lst2[n-1-i]
            ans = max(ans, total + kind * kind)
            flag = False
            j += 1
        else:
            j += 1
print (ans)
