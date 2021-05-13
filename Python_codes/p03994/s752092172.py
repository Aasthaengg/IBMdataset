s = input()
K = int(input())
alpha = "bcdefghijklmnopqrstuvwxyza"
dic = {j : 25 - i for i, j in enumerate(alpha)}
inv_dic = {j : i for i, j in dic.items()}
s_ls = [dic[_s] for _s in s]
remain = K
ind = 0
len_s = len(s)
while ind < len_s and remain > 0:
    _s = s_ls[ind]
    if _s <= remain:
        remain -= _s
        s_ls[ind] = 0
    ind += 1
if remain > 0:
    s_ls[ind - 1] = (s_ls[ind - 1] - remain) % 26
print("".join([inv_dic[_s] for _s in s_ls]))