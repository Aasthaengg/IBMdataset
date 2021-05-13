import copy
N = int(input())
S = input()

cnt = [0]*10
for x in S:
    cnt[int(x)] += 1

tars = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            tars.append(str(i)+str(j)+str(k))

ans = 0
for tar in tars:
    id = 0
    copy_cnt = copy.copy(cnt)
    if copy_cnt[int(tar[0])] == 0 or copy_cnt[int(tar[1])] == 0 or copy_cnt[int(tar[2])] == 0:
        continue
    while S[id] != tar[0]:
        copy_cnt[int(S[id])] -= 1
        id += 1
    copy_cnt[int(S[id])] -= 1
    id += 1
    if copy_cnt[int(tar[1])] == 0 or copy_cnt[int(tar[2])] == 0:
        continue
    while S[id] != tar[1]:
        copy_cnt[int(S[id])] -= 1
        id += 1
    copy_cnt[int(S[id])] -= 1
    if copy_cnt[int(tar[2])] == 0:
        continue
    else:
        ans += 1

print(ans)