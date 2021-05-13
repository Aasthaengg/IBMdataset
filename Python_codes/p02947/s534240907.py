# 問題：https://atcoder.jp/contests/abc137/tasks/abc137_c

n = int(input())
s_dict = {}
res = 0
for i in range(n):
    word = ''.join(sorted(input()))
    if word in s_dict.keys():
        res += s_dict[word]
        s_dict[word] += 1
    else:
        s_dict[word] = 1

print(res)

