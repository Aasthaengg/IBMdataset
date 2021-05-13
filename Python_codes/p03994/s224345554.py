import itertools

s = input()
K = int(input())

alp = list('abcdefghijklmnopqrstuvwxyz')

index_list = [alp.index(s[i]) for i in range(len(s))]

cnt_list = []
for j in index_list:
    if j > 0:
        cnt_list.append(26-j)
    else:
        cnt_list.append(0)

s_list = list(s)

if sum(cnt_list) <= K:
    num = (K - sum(cnt_list)) % 26
    l = "a" * (len(s)-1) + alp[num]
    print(l)
else:
    i = 0
    for i in range(len(s)):
        if i == len(s)-1:
            if K >= cnt_list[i]:
                num = (K - cnt_list[i]) % 26
                s_list[i] = alp[num]
            else:
                s_list[i] = alp[K-cnt_list[i]]
        elif K >= cnt_list[i]:
            K -= cnt_list[i]
            s_list[i] = 'a'
        else:
            pass
    ans = ''.join(s_list)
    print(ans)