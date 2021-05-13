# Problem - サイコロ

# input
t, s, e, w, n, b = map(int, input().split())
p_num = int(input())

# initialization
dice_dic = {}
dice_dic[t] = {s:e, e:n, n:w, w:s}
dice_dic[b] = {n:e, w:n, s:w, e:s}
dice_dic[s] = {e:t, t:w, w:b, b:e}
dice_dic[n] = {t:e, e:b, b:w, w:t}
dice_dic[e] = {s:b, b:n, n:t, t:s}
dice_dic[w] = {s:t, t:n, n:b, b:s}

# process
for i in range(p_num):
    in_1, in_2 = map(int, input().split())
    print(dice_dic[in_1][in_2])

