n, k = map(int, input().split())
ps = list(map(int, input().split()))
cs = list(map(int, input().split()))

to_do = []
res = -float('inf')
for i in range(1,n+1):
    tmp_idx = i
    tmp_val = 0
    tmp_dic = {i:(0,0,i)}
    for j in range(1,min(n+1,k+1)):
        tmp_idx = ps[tmp_idx-1]
        tmp_val += cs[tmp_idx-1]
        res = max(res,tmp_val)
        if tmp_idx not in tmp_dic:
            tmp_dic[tmp_idx] = (j,tmp_val,tmp_idx)
        else:
            if tmp_val > tmp_dic[tmp_idx][1]:
                to_do.append([i,tmp_dic[tmp_idx][0],tmp_dic[tmp_idx][2],tmp_dic[tmp_idx][1],j-tmp_dic[tmp_idx][0],tmp_val-tmp_dic[tmp_idx][1]])
            break

for do in to_do:
    itr = (k - do[1]) // do[4]
    if itr > 0:
        itr -= 1
    remain = k - do[1] - do[4] * itr
    tmp_res = do[3] + itr * do[5]
    res = max(res,tmp_res)
    now = do[2]
    for i in range(remain):
        now = ps[now-1]
        tmp_res += cs[now-1]
        res = max(res, tmp_res)
print(res)