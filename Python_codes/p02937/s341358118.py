from bisect import bisect_left

S = list(input())
T = list(input())
dict_s = {}
for i,val in enumerate(S):
    if val in dict_s:
        dict_s[val].append(i)
    else:
        dict_s[val] = [i]

l_cunt = 0
now_point = -1
for i,val in enumerate(T):
    if val in dict_s:
        tmp_point = bisect_left(dict_s[val],now_point)
        if tmp_point == len(dict_s[val]):
            l_cunt += 1
            tmp_point = 0
        now_point = dict_s[val][tmp_point]+1
    else:
        print(-1)
        exit()

print(l_cunt*len(S)+now_point)