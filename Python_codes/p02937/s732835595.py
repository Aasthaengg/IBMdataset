import string
import bisect

s = str(input())
t = str(input())
len_s = len(s)
len_t = len(t)

s_alpha_ind = {x:[] for x in string.ascii_lowercase}

for i in range(len_s):
    s_alpha_ind[s[i]].append(i+1)

ans = 0
now_s_ind = 0
for i in range(len_t):
    now_t = t[i]
    if len(s_alpha_ind[now_t]) == 0:
        ans = -1
        break
    else:
        # print('now s_ind is: '+ str(now_s_ind))
        # print('-'*30)
        # print('now_t is: ' + str(now_t))

        # 二分探索で、now_s_indよりも大きな値を探す
        # なければ最初の値を返す
        Inds = s_alpha_ind[now_t]
        ind = bisect.bisect_right(Inds, now_s_ind)
        # print('Inds is :')
        # print(Inds)
        # print('ind is:' + str(ind))

        if ind == len(Inds):
            ans += (len_s - now_s_ind + Inds[0])
            if i == 0:
                ans -= len_s
            now_s_ind = Inds[0]
        else:
            ans += Inds[ind] - now_s_ind
            now_s_ind = Inds[ind]
        # print('ans is:' +  str(ans))


print(ans)